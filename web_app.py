import streamlit as st
import pandas as pd
import os
import json
from app.services.data_service import DataService
from app.services.price_service import PriceService
from app.services.analytics_service import AnalyticsService
from app.services.user_service import UserService
from app.config import settings
from app.path_utils import resource_path
from streamlit_js_eval import streamlit_js_eval

# --- Page Configuration ---
st.set_page_config(
    page_title="EVE Echoes Planetary Mining Optimizer",
    page_icon="🪐",
    layout="wide"
)

# Google Analytics (gtag.js)
st.markdown(
    """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-NJMX7FMVNW"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);} 
      gtag('js', new Date());
      gtag('config', 'G-NJMX7FMVNW');
    </script>
    """,
    unsafe_allow_html=True,
)

# --- Demo mode (no authentication) ---
user_service = UserService(user_file_path=resource_path("app/secure/users.json"))
st.session_state.authentication_status = True
st.session_state.username = "guest"

def login_form():
    # Hero Section for Login
    st.markdown("""
    <div style="
        background: linear-gradient(50deg, #D4D9DB 0%, #D4D9DB 100%);
        padding: 2rem;
        border-radius: 5px;
        margin-bottom: 1rem;
        text-align: center;
        color: black;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    ">
        <h1 style="font-size: 1.5rem; margin-bottom: 1rem; text-shadow: 1px 1px 2px rgba(0,0,0,0.3);">
            🪐 EVE Echoes Planetary Mining Optimizer
        </h1>
        <p style="font-size: 1.1rem; opacity: 0.9; margin-bottom: 0;">
            Log in to start optimizing planetary mining operations
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Two column layout: Features on left, Login on right
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Features from README.md lines 6-12
        st.markdown("### 🚀 Features")
        
        # Feature Card 1
        st.markdown("""
        <div style="
            background: #8E8E93;
            padding: 0.6rem;
            border-radius: 9px;
            margin-bottom: 0.4rem;
            color: white;
            box-shadow: 0 2.4px 12px rgba(0,0,0,0.1);
            border-left: 3px solid #ffffff;
        ">
            <h3 style="margin: 0 0 0.4rem 0; font-size: 1.1rem;">🪐 Planetary Resource Analysis</h3>
            <p style="margin: 0; opacity: 0.9; font-size: 0.95rem;">
                Analyze resources across all systems, constellations, and regions
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature Card 2
        st.markdown("""
        <div style="
            background: #8E8E93;
            padding: 0.6rem;
            border-radius: 9px;
            margin-bottom: 0.4rem;
            color: white;
            box-shadow: 0 2.4px 12px rgba(0,0,0,0.1);
            border-left: 3px solid #ffffff;
        ">
            <h3 style="margin: 0 0 0.4rem 0; font-size: 1.1rem;">💰 Price Management</h3>
            <p style="margin: 0; opacity: 0.9; font-size: 0.95rem;">
                Import and manage custom price lists
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature Card 3
        st.markdown("""
        <div style="
            background: #8E8E93;
            padding: 0.6rem;
            border-radius: 9px;
            margin-bottom: 0.4rem;
            color: white;
            box-shadow: 0 2.4px 12px rgba(0,0,0,0.1);
            border-left: 3px solid #ffffff;
        ">
            <h3 style="margin: 0 0 0.4rem 0; font-size: 1.1rem;">📊 Mining Units Optimization</h3>
            <p style="margin: 0; opacity: 0.9; font-size: 0.95rem;">
                Calculate optimal mining unit placement
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature Card 4
        st.markdown("""
        <div style="
            background: #8E8E93;
            padding: 0.6rem;
            border-radius: 9px;
            margin-bottom: 0.4rem;
            color: white;
            box-shadow: 0 2.4px 12px rgba(0,0,0,0.1);
            border-left: 3px solid #ffffff;
        ">
            <h3 style="margin: 0 0 0.4rem 0; font-size: 1.1rem;">🚀 Logistics Planning</h3>
            <p style="margin: 0; opacity: 0.9; font-size: 0.95rem;">
                Plan cargo runs based on ship capacity
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature Card 5
        st.markdown("""
        <div style="
            background: #8E8E93;
            padding: 0.6rem;
            border-radius: 9px;
            margin-bottom: 0.4rem;
            color: white;
            box-shadow: 0 2.4px 12px rgba(0,0,0,0.1);
            border-left: 3px solid #ffffff;
        ">
            <h3 style="margin: 0 0 0.4rem 0; font-size: 1.1rem;">📈 Analytics & Reports</h3>
            <p style="margin: 0; opacity: 0.9; font-size: 0.95rem;">
                Detailed profitability analysis and reports
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # Feature Card 6
        st.markdown("""
        <div style="
            background: #8E8E93;
            padding: 0.6rem;
            border-radius: 9px;
            margin-bottom: 0.4rem;
            color: white;
            box-shadow: 0 2.4px 12px rgba(0,0,0,0.1);
            border-left: 3px solid #ffffff;
        ">
            <h3 style="margin: 0 0 0.4rem 0; font-size: 1.1rem;">👥 Multi-user Support</h3>
            <p style="margin: 0; opacity: 0.9; font-size: 0.95rem;">
                Secure user authentication and personal data storage
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        # Login Form with styling
        st.markdown("### 🔐 Login")
        
        with st.form("login_form"):
            username = st.text_input("Username", placeholder="Enter username")
            password = st.text_input("Password", type="password", placeholder="Enter password")
            submitted = st.form_submit_button("Login", type="primary", use_container_width=True)
            if submitted:
                if user_service.verify_user(username, password):
                    st.session_state.authentication_status = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("❌ Invalid username or password")

        if settings.ALLOW_GUEST:
            st.markdown("---")
            if st.button("Continue as Guest (no persistence)", use_container_width=True):
                st.session_state.authentication_status = True
                st.session_state.username = "guest"
                st.rerun()
        
        # Support section in the right column
        st.markdown("### 💰 Support")
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            padding: 0.6rem;
            border-radius: 6px;
            text-align: center;
            box-shadow: 0 1.6px 9px rgba(0,0,0,0.1);
            border: 1.2px solid #ffd700;
        ">
            <h4 style="color: #d63384; margin-bottom: 0.4rem; font-size: 0.9rem;">💎 Support the Developer</h4>
            <p style="margin-bottom: 0.4rem; color: #333; font-size: 0.7rem;">
                If you find this tool helpful, please consider supporting!
            </p>
            <div style="
                background: rgba(255,255,255,0.3);
                padding: 0.32rem;
                border-radius: 4.8px;
                margin: 0.4rem 0;
            ">
                <h5 style="margin: 0; color: #d63384; font-size: 0.7rem;">ISK Donations:</h5>
                <h4 style="margin: 0.12rem 0; color: #333; font-size: 0.8rem;">lawrokhPL</h4>
                <p style="margin: 0; color: #666; font-size: 0.6rem;">in EVE Echoes</p>
            </div>
            <p style="margin: 0; font-style: italic; color: #666; font-size: 0.6rem;">
                Thank you! o7
            </p>
        </div>
        """, unsafe_allow_html=True)

def registration_form():
    # Black header bar with white centered text
    st.markdown("""
    <div style="
        background: #000000;
        padding: 1rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        text-align: center;
        color: white;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    ">
        <h2 style="margin: 0; font-size: 1.5rem; color: white;">📝 Registration</h2>
        <p style="margin: 0.5rem 0 0 0; color: #cccccc; font-size: 1rem;">Create your account to get started</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Load Privacy Policy
    try:
        with open(resource_path("PRIVACY_POLICY.md"), "r", encoding="utf-8") as f:
            privacy_policy_md = f.read()
    except:
        privacy_policy_md = "Privacy Policy: Your data is stored locally and securely. We do not share your information with third parties."
    
    # Create two columns for better layout
    col1, col2 = st.columns([2, 1])
    
    with col1:
        with st.form("registration_form"):
            username = st.text_input("Username", placeholder="Enter username")
            password = st.text_input("Password", type="password", placeholder="Enter password")
            
            st.markdown("### 📋 Privacy Policy")
            st.info("By registering, you agree to our Privacy Policy. Your data is stored securely and never shared with third parties.")
            
            privacy_policy_accepted = st.checkbox("I agree to the Privacy Policy")
                
            submitted = st.form_submit_button("Register", type="primary", use_container_width=True)
            if submitted:
                if not username or not password:
                    st.error("❌ Please enter both username and password.")
                elif not privacy_policy_accepted:
                    st.error("❌ You must accept the Privacy Policy to register.")
                else:
                    success, message = user_service.register_user(username, password)
                    if success:
                        st.success("✅ " + message)
                        st.info("You can now login with your credentials.")
                    else:
                        st.error("❌ " + message)
    
    with col2:
        st.markdown("### 💰 Support")
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            padding: 0.6rem;
            border-radius: 6px;
            text-align: center;
            box-shadow: 0 1.6px 9px rgba(0,0,0,0.1);
            border: 1.2px solid #ffd700;
        ">
            <h4 style="color: #d63384; margin-bottom: 0.4rem; font-size: 0.9rem;">💎 Support the Developer</h4>
            <p style="margin-bottom: 0.4rem; color: #333; font-size: 0.7rem;">
                If you find this tool helpful, please consider supporting!
            </p>
            <div style="
                background: rgba(255,255,255,0.3);
                padding: 0.32rem;
                border-radius: 4.8px;
                margin: 0.4rem 0;
            ">
                <h5 style="margin: 0; color: #d63384; font-size: 0.7rem;">ISK Donations:</h5>
                <h4 style="margin: 0.12rem 0; color: #333; font-size: 0.8rem;">lawrokhPL</h4>
                <p style="margin: 0; color: #666; font-size: 0.6rem;">in EVE Echoes</p>
            </div>
            <p style="margin: 0; font-style: italic; color: #666; font-size: 0.6rem;">
                Thank you! o7
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- Main App Logic ---
def main_app():
    username = st.session_state.username
    
    # --- Load User Preferences ---
    if 'user_prefs' not in st.session_state:
        # Dla guest nie zapisujemy na serwerze; tylko localStorage
        if username == "guest":
            st.session_state.user_prefs = {}
        else:
            st.session_state.user_prefs = user_service.load_user_preferences(username)

    # Jednorazowe wczytanie preferencji z localStorage (per urządzenie/przeglądarka)
    if not st.session_state.get('local_storage_prefs_loaded'):
        try:
            ls_key = f"eve_prefs_{username}"
            stored = streamlit_js_eval(js_expressions=f"localStorage.getItem('{ls_key}')", key=f"get_{ls_key}")
            if stored:
                try:
                    parsed = json.loads(stored)
                    if isinstance(parsed, dict):
                        # Zmerguj z istniejącymi preferencjami z pliku
                        st.session_state.user_prefs.update(parsed)
                except Exception:
                    pass
        except Exception:
            pass
        st.session_state.local_storage_prefs_loaded = True

    def _save_prefs_to_local_storage():
        try:
            ls_key = f"eve_prefs_{username}"
            prefs_json = json.dumps(st.session_state.user_prefs)
            # Wstaw jako string literal, bezpiecznie uciecz znaki
            prefs_js_string = prefs_json.replace("\\", "\\\\").replace("'", "\\'")
            streamlit_js_eval(js_expressions=f"localStorage.setItem('{ls_key}', '{prefs_js_string}')", key=f"set_{ls_key}", want_output=False)
        except Exception:
            pass

    def save_prefs():
        """Callback to save preferences."""
        if username != "guest":
            user_service.save_user_preferences(username, st.session_state.user_prefs)
        _save_prefs_to_local_storage()

    def set_pref(pref_key, value):
        """Utility to persist a single preference immediately."""
        st.session_state.user_prefs[pref_key] = value
        if username != "guest":
            user_service.save_user_preferences(username, st.session_state.user_prefs)
        _save_prefs_to_local_storage()

    def autoload_latest_prices(current_username: str, svc: "PriceService") -> None:
        """Load default prices from ceny.csv if available, else newest CSV in user's folder.
        Accepts CSV with columns: resource + (price | average/buy)."""
        try:
            import csv
            def _csv_to_dict(path: str):
                try:
                    with open(path, newline='', encoding='utf-8') as f:
                        reader = csv.DictReader(f)
                        name_key = None
                        for k in reader.fieldnames or []:
                            kk = (k or '').strip().lower()
                            if kk in ("resource", "name"):
                                name_key = k
                                break
                        if not name_key:
                            return {}
                        rows = list(reader)
                        def get_num(row, keys):
                            for key in keys:
                                if key in row and row[key] not in (None, ""):
                                    try:
                                        return float(row[key])
                                    except Exception:
                                        continue
                            return 0.0
                        prices = {}
                        for r in rows:
                            res = str(r.get(name_key, "")).strip()
                            if not res:
                                continue
                            val = get_num(r, ["average", "avg", "price", "buy"])  # prefer avg/price
                            prices[res] = val
                        return prices
                except Exception:
                    return {}
            # 1) prefer explicit default ceny.csv paths
            candidates = [
                os.path.join(settings.DATA_ROOT, 'user_data', 'lawrokh', 'price_imports', 'ceny.csv'),
                os.path.join(settings.DATA_ROOT, 'price_imports', 'ceny.csv'),
                resource_path(os.path.join('data', 'price_imports', 'ceny.csv')),
                resource_path(os.path.join('data', 'ceny.csv')),
            ]
            chosen_path = None
            for c in candidates:
                if os.path.exists(c):
                    chosen_path = c
                    break
            # 2) otherwise pick newest user CSV
            if chosen_path is None:
                # 2a) packaged CSVs in repo (data/price_imports)
                pkg_imports = resource_path(os.path.join('data', 'price_imports'))
                if os.path.isdir(pkg_imports):
                    pkg_csvs = [os.path.join(pkg_imports, f) for f in os.listdir(pkg_imports) if f.endswith('.csv')]
                    if pkg_csvs:
                        chosen_path = max(pkg_csvs, key=lambda p: os.path.getmtime(p))
            if chosen_path is None:
                # 2b) newest user CSV
                imports_dir = os.path.join(settings.DATA_ROOT, "user_data", current_username, "price_imports")
                if os.path.isdir(imports_dir):
                    csvs = [os.path.join(imports_dir, f) for f in os.listdir(imports_dir) if f.endswith(".csv")]
                    if csvs:
                        chosen_path = max(csvs, key=lambda p: os.path.getmtime(p))
            if chosen_path and os.path.exists(chosen_path):
                price_dict = _csv_to_dict(chosen_path)
                if price_dict:
                    svc.update_multiple_prices(price_dict)
                    try:
                        svc.save_prices()
                    except Exception:
                        pass
            else:
                svc.load_prices()
        except Exception:
            # Silent fallback
            try:
                svc.load_prices()
            except Exception:
                pass

    # --- Data Loading ---
    @st.cache_resource(show_spinner=f"Loading data for {username}...")
    def load_user_services(username):
        """Loads all necessary services for a given user."""
        # Use DATA_ROOT for writable paths (supports Fly.io persistent volume)
        user_data_root = os.path.join(settings.DATA_ROOT, "user_data", username)
        data_path = resource_path(os.path.join("data", "eve_planets.parquet"))
        prices_path = os.path.join(user_data_root, "prices.json")
        mining_units_path = os.path.join(user_data_root, "mining_units.json")

        # Create user-specific directories if they don't exist
        os.makedirs(user_data_root, exist_ok=True)
        os.makedirs(os.path.join(user_data_root, "price_imports"), exist_ok=True)
        
        data_service = DataService(data_path, mining_units_path)
        data_service.load_data()
        
        price_service = PriceService(prices_path)
        autoload_latest_prices(username, price_service)
        analytics_service = AnalyticsService(data_service, price_service)
        
        return data_service, price_service, analytics_service

    data_service, price_service, analytics_service = load_user_services(username)

    # --- Sidebar ---
    with st.sidebar:
        st.title(f"Welcome, {username}")
        if st.button("Logout"):
            st.session_state.authentication_status = None
            st.session_state.username = None
            st.rerun()
        
        st.header("Filters")
        
        # --- Price loading info ---
        try:
            prices_count = len(price_service.get_all_prices())
            st.caption(f"Current prices loaded: {prices_count}")
        except Exception:
            pass

        # --- Persisted Filters ---
        # Search
        search_query = st.text_input(
            "Search System, Constellation, or Region",
            value=st.session_state.user_prefs.get('search_query', ''),
            key='search_query',
            on_change=lambda: set_pref('search_query', st.session_state.get('search_query', ''))
        )
        
        all_resources_list = data_service.get_all_resources()
        selected_resources = st.multiselect(
            "Resource",
            all_resources_list,
            default=st.session_state.user_prefs.get('resource_filter', []),
            key="resource_filter",
            on_change=lambda: set_pref('resource_filter', st.session_state.get('resource_filter', []))
        )

        regions = data_service.get_regions()
        selected_regions = st.multiselect(
            "Region",
            regions,
            default=st.session_state.user_prefs.get('region_filter', []),
            key="region_filter",
            on_change=lambda: set_pref('region_filter', st.session_state.get('region_filter', []))
        )
        
        if not selected_regions:
            constellations_list = data_service.get_constellations()
        else:
            constellations_list = data_service.get_constellations(selected_regions)
        selected_constellations = st.multiselect(
            "Constellation",
            constellations_list,
            default=st.session_state.user_prefs.get('constellation_filter', []),
            key="constellation_filter",
            on_change=lambda: set_pref('constellation_filter', st.session_state.get('constellation_filter', []))
        )

        if not selected_constellations:
            systems_list = data_service.get_systems()
        else:
            systems_list = data_service.get_systems(selected_constellations)
        selected_systems = st.multiselect(
            "System",
            systems_list,
            default=st.session_state.user_prefs.get('system_filter', []),
            key="system_filter",
            on_change=lambda: set_pref('system_filter', st.session_state.get('system_filter', []))
        )

        st.divider()
        st.header("Logistics Input")
        
        st.session_state.user_prefs['ship_cargo_capacity'] = st.number_input(
            "Ship Cargo Capacity (m³)", 
            min_value=0, 
            value=st.session_state.user_prefs.get('ship_cargo_capacity', 10000), 
            step=100,
            on_change=save_prefs,
            key='pref_ship_cargo'
        )
        st.session_state.user_prefs['planetary_storage_capacity'] = st.number_input(
            "Planetary Storage Capacity (m³)", 
            min_value=0, 
            value=st.session_state.user_prefs.get('planetary_storage_capacity', 920), 
            step=10,
            on_change=save_prefs,
            key='pref_planetary_storage'
        )
        
        st.divider()
        st.markdown("""
        ### 💰 Support Development
        **ISK Donations:**  
        **lawrokhPL** in EVE Echoes
        
        Thank you! o7
        """)

    # --- Master DataFrame Preparation ---
    master_df_key = f'master_df_{username}'
    if master_df_key not in st.session_state:
        all_planets = data_service.get_all_planets()
        resource_data = []
        for planet in all_planets:
            for resource in planet.resources:
                resource_data.append({
                    "id": f"{resource.planet_id}_{resource.resource}",
                    "System": planet.system,
                    "Constellation": planet.constellation,
                    "Region": planet.region,
                    "Planet": planet.name,
                    "Type": planet.planet_type.value,
                    "Resource": resource.resource,
                    "Richness": resource.richness.value,
                    "Output/h/unit": resource.output,
                    "obj": resource 
                })
        st.session_state[master_df_key] = pd.DataFrame(resource_data)

    master_df = st.session_state[master_df_key]

    # --- Main Page ---
    st.title("🪐 EVE Echoes Planetary Mining Optimizer")

    # Toolbar w prawym górnym rogu: eksport/import ustawień
    tcol1, tcol2 = st.columns([8, 2])
    with tcol2:
        with st.popover("Settings Sync"):
            st.caption("Export/Import your current settings for use on another browser.")
            try:
                prefs_json = json.dumps(st.session_state.user_prefs, ensure_ascii=False, indent=2)
            except Exception:
                prefs_json = "{}"
            st.download_button(
                label="Export settings (JSON)",
                data=prefs_json.encode("utf-8"),
                file_name=f"{username}_settings.json",
                mime="application/json",
                use_container_width=True,
            )

            uploaded_prefs = st.file_uploader("Import settings (JSON)", type=["json"], accept_multiple_files=False)
            if uploaded_prefs is not None:
                try:
                    imported = json.loads(uploaded_prefs.read().decode("utf-8"))
                    if isinstance(imported, dict):
                        st.session_state.user_prefs.update(imported)
                        save_prefs()
                        st.success("Settings imported successfully.")
                        st.rerun()
                    else:
                        st.error("Invalid JSON content. Expected an object with preferences.")
                except Exception as e:
                    st.error(f"Failed to import settings: {e}")

    # Filtering logic on the master dataframe
    filtered_df = master_df
    if selected_regions:
        filtered_df = filtered_df[filtered_df['Region'].isin(selected_regions)]
    if selected_constellations:
        filtered_df = filtered_df[filtered_df['Constellation'].isin(selected_constellations)]
    if selected_systems:
        filtered_df = filtered_df[filtered_df['System'].isin(selected_systems)]
    if search_query:
        query = search_query.lower()
        filtered_df = filtered_df[
            filtered_df['System'].fillna('').str.lower().str.contains(query) |
            filtered_df['Constellation'].fillna('').str.lower().str.contains(query) |
            filtered_df['Region'].fillna('').str.lower().str.contains(query)
        ]
    if selected_resources:
        filtered_df = filtered_df[filtered_df['Resource'].isin(selected_resources)]

    # Prepare data for display
    # Perform calculations on the filtered dataframe for performance
    df = filtered_df
    
    # Update mining units from objects, as they can change
    df['Mining Units'] = df['obj'].apply(lambda r: r.mining_units)

    prices = price_service.get_all_prices()
    price_map = df['Resource'].map(prices).fillna(0)
    
    df["Value/h/unit"] = df["Output/h/unit"] * price_map
    df["Total Value/h"] = df["Value/h/unit"] * df["Mining Units"]
    
    if not df.empty:
        df = df.set_index("id")

    # Calculate a separate dataframe for summaries that ignores filters
    df_all = master_df.copy()
    df_all['Mining Units'] = df_all['obj'].apply(lambda r: r.mining_units)
    price_map_all = df_all['Resource'].map(prices).fillna(0)
    df_all["Value/h/unit"] = df_all["Output/h/unit"] * price_map_all
    df_all["Total Value/h"] = df_all["Value/h/unit"] * df_all["Mining Units"]
    if not df_all.empty:
        df_all = df_all.set_index("id")

    # Display Analysis Table with Data Editor
    st.info("You can directly edit the 'Mining Units' column below. Click the 'Update Mining Units' button to apply changes.")

    if not df.empty:
        column_config = {
            "id": None, # Ukryj kolumnę ID
            "Mining Units": st.column_config.NumberColumn(
                "Mining Units",
                help="Set the number of mining units for this resource.",
                min_value=0, step=1, format="%d"
            ),
             "Value/h/unit": st.column_config.NumberColumn(format="%.2f"),
            "Total Value/h": st.column_config.NumberColumn(format="%.2f"),
        }
        
        # Sortowanie i przygotowanie kolumn do wyświetlenia
        df_display = df.sort_values(by="Total Value/h", ascending=False)
        display_cols = ["Region", "Constellation", "System", "Planet", "Type", "Resource", "Richness", "Output/h/unit", "Mining Units", "Value/h/unit", "Total Value/h"]
        
        # Upewnij się, że wszystkie kolumny istnieją przed ich wyświetleniem
        final_display_cols = [col for col in display_cols if col in df_display.columns]

        edited_df = st.data_editor(
            df_display[final_display_cols],
            column_config=column_config,
            use_container_width=True,
            key="data_editor",
            hide_index=True # Ukryj domyślny indeks numeryczny
        )

        _, button_col = st.columns([4, 1])
        with button_col:
            if st.button("Update Mining Units"):
                changes_made = False
                try:
                    # Iterujemy po indeksie (to są nasze id) i kolumnie 'Mining Units'
                    for resource_id, row in edited_df.iterrows():
                        if "Mining Units" not in row:
                            continue
                        new_units_val = row.get("Mining Units", 0)
                        try:
                            new_units = int(new_units_val)
                        except (ValueError, TypeError):
                            new_units = 0
                        # Aktualizuj obiekt zasobu powiązany z tym wierszem
                        if resource_id in df.index:
                            resource_obj = df.loc[resource_id, 'obj']
                            if getattr(resource_obj, 'mining_units', 0) != new_units:
                                resource_obj.mining_units = new_units
                                changes_made = True
                except Exception:
                    pass

                if changes_made:
                    data_service.save_mining_units()
                    data_service.update_dataframe_mining_units()
                    st.toast("Jednostki wydobywcze zaktualizowane!", icon="✅")
                    st.rerun()
                else:
                    st.toast("Brak zmian do zaktualizowania.", icon="ℹ️")
    else:
        st.info("No data to display for the selected filters.")


    # --- Tabs for other functionalities ---
    tab1, tab2, tab3 = st.tabs(["Summaries", "Price Management", "POS Fuel Planner"]) 

    with tab1:
        st.header("Income & Logistics Summaries")

        # --- Tax Input ---
        st.session_state.user_prefs['tax_rate'] = st.number_input(
            "Broker/Transaction Tax (%)", 
            min_value=0.0, 
            max_value=100.0, 
            value=st.session_state.user_prefs.get('tax_rate', 8.0),
            step=0.1,
            format="%.2f",
            help="Enter your total tax rate (Broker Fee + Sales Tax) as a percentage.",
            on_change=save_prefs,
            key='pref_tax_rate'
        )

        # Create a single summary dataframe for all calculations (ignores filters)
        summary_df = df_all[df_all['Mining Units'] > 0].copy()

        if not summary_df.empty:
            # --- CALCULATIONS (GROSS) ---
            summary_df['Gross Daily Income'] = summary_df['Total Value/h'] * 24
            summary_df['Gross Weekly Income'] = summary_df['Total Value/h'] * 24 * 7
            summary_df['Gross Monthly Income'] = summary_df['Total Value/h'] * 24 * 30
            
            # --- CALCULATIONS (NET) ---
            tax_rate = st.session_state.user_prefs.get('tax_rate', 8.0)
            tax_multiplier = 1 - (tax_rate / 100)
            summary_df['Net Daily Income'] = summary_df['Gross Daily Income'] * tax_multiplier
            summary_df['Net Weekly Income'] = summary_df['Gross Weekly Income'] * tax_multiplier
            summary_df['Net Monthly Income'] = summary_df['Gross Monthly Income'] * tax_multiplier

            # Volume
            RESOURCE_UNIT_VOLUME = 0.01  # m3
            summary_df['Hourly Volume (m3)'] = summary_df['Output/h/unit'] * summary_df['Mining Units'] * RESOURCE_UNIT_VOLUME

            # --- DISPLAY INCOME ---
            st.subheader("Income Summary")
            income_display_cols = ["Region", "Constellation", "System", "Planet", "Resource", "Mining Units", "Net Daily Income"]
            display_income_df = summary_df[income_display_cols].copy()
            # Format for display
            display_income_df["Net Daily Income"] = display_income_df["Net Daily Income"].map('{:,.2f}'.format)
            
            st.dataframe(display_income_df.sort_values(by="Net Daily Income", key=lambda x: pd.to_numeric(x.str.replace(',','')), ascending=False), use_container_width=True, hide_index=True)
            
            # Totals
            total_net_daily = summary_df['Net Daily Income'].sum()
            total_net_weekly = summary_df['Net Weekly Income'].sum()
            total_net_monthly = summary_df['Net Monthly Income'].sum()
            
            i_col1, i_col2, i_col3 = st.columns(3)
            i_col1.metric("Total Net Daily Income", f"{total_net_daily:,.2f} ISK")
            i_col2.metric("Total Net Weekly Income", f"{total_net_weekly:,.2f} ISK")
            i_col3.metric("Total Net Monthly Income", f"{total_net_monthly:,.2f} ISK")


            st.divider()

            # --- FINAL PROFIT CALCULATION ---
            st.subheader("Final Profit Summary")
            
            st.session_state.user_prefs['pos_cost'] = st.number_input(
                "Corporation POS Cost (Monthly)",
                min_value=0,
                value=st.session_state.user_prefs.get('pos_cost', 1500000000),
                step=1000000,
                format="%d",
                help="Enter the total monthly cost for maintaining your Corporation POS.",
                on_change=save_prefs,
                key='pref_pos_cost'
            )

            pos_cost = st.session_state.user_prefs.get('pos_cost', 1500000000)
            final_monthly_profit = total_net_monthly - pos_cost

            f_col1, f_col2, f_col3 = st.columns(3)
            f_col1.metric("Net Monthly Income", f"{total_net_monthly:,.2f} ISK")
            f_col2.metric("Corporation POS Cost", f"{pos_cost:,.2f} ISK", delta_color="inverse")
            f_col3.metric("Final Monthly Profit", f"{final_monthly_profit:,.2f} ISK")


            st.divider()

            # --- DISPLAY LOGISTICS ---
            st.subheader("Logistics Summary")
            
            # --- Planetary Storage Fill Time (per Planet) ---
            st.markdown("#### Planetary Storage")
            if st.session_state.user_prefs['planetary_storage_capacity'] > 0:
                planet_volume_summary = summary_df.groupby(['System', 'Planet'])['Hourly Volume (m3)'].sum().reset_index()
                planet_volume_summary = planet_volume_summary[planet_volume_summary['Hourly Volume (m3)'] > 0]

                if not planet_volume_summary.empty:
                    planet_volume_summary['Time to Fill (hours)'] = st.session_state.user_prefs['planetary_storage_capacity'] / planet_volume_summary['Hourly Volume (m3)']
                    
                    display_planet_summary = planet_volume_summary.copy()
                    display_planet_summary['Hourly Volume (m3)'] = display_planet_summary['Hourly Volume (m3)'].map('{:,.2f}'.format)
                    display_planet_summary['Time to Fill (hours)'] = display_planet_summary['Time to Fill (hours)'].map('{:,.2f}'.format)
                    
                    st.dataframe(
                        display_planet_summary[['System', 'Planet', 'Hourly Volume (m3)', 'Time to Fill (hours)']],
                        use_container_width=True,
                        hide_index=True,
                    )
            else:
                st.info("Set planetary storage capacity to see fill times.")

            # --- Transport Summary ---
            st.markdown("#### Transport")
            if st.session_state.user_prefs['ship_cargo_capacity'] > 0:
                total_hourly_volume = summary_df['Hourly Volume (m3)'].sum()
                total_daily_volume = total_hourly_volume * 24

                collection_frequency_days = st.session_state.user_prefs['ship_cargo_capacity'] / total_daily_volume if total_daily_volume > 0 else float('inf')

                def format_frequency(days):
                    if days == float('inf'): return "N/A"
                    total_seconds = int(days * 24 * 3600)
                    if total_seconds <= 0: return "N/A"
                    d = total_seconds // 86400; h = (total_seconds % 86400) // 3600; m = (total_seconds % 3600) // 60
                    parts = []
                    if d > 0: parts.append(f"{d}d")
                    if h > 0: parts.append(f"{h}h")
                    if m > 0: parts.append(f"{m}m")
                    return " ".join(parts) if parts else "< 1m"
                
                frequency_str = format_frequency(collection_frequency_days)

                l_col1, l_col2, l_col3 = st.columns(3)
                l_col1.metric("Ship Cargo", f"{st.session_state.user_prefs['ship_cargo_capacity']:,.0f} m³")
                l_col2.metric("Total Daily Volume", f"{total_daily_volume:,.2f} m³")
                l_col3.metric("Collection Frequency", f"Every {frequency_str}")
            else:
                st.info("Set ship cargo capacity to see transport summary.")

        else:
            st.info("Assign mining units to see income and logistics summaries.")

    with tab2:
        st.header("Price Management")

        # --- Top Section: Import, Export, Load ---
        st.subheader("Manage Price Files")

        # Export Button (unchanged)
        prices_df = pd.DataFrame(price_service.get_all_prices().items(), columns=["resource", "price"])
        st.download_button(label="Export Current Prices to CSV", data=prices_df.to_csv(index=False).encode('utf-8'), file_name="current_prices.csv", mime="text/csv")

        # Import Uploader
        uploaded_file = st.file_uploader("Upload a new price CSV (import into DB; no file stored)", type="csv")
        if uploaded_file is not None:
            try:
                new_prices_df = pd.read_csv(uploaded_file)
                if settings.DATA_BACKEND == "sql":
                    try:
                        from app.services.user_service_sql import SQLUserService
                        uid = SQLUserService().get_user_id(username)
                    except Exception:
                        uid = None
                    # Save history rows (resource,buy,sell,average[,date]) and update current cache from 'average' or 'buy'
                    from datetime import datetime
                    price_service.import_prices_dataframe(new_prices_df, user_id=uid, price_date=datetime.utcnow())
                    # Update live cache from avg/buy if present, else 'price'
                    price_dict = {}
                    if 'average' in new_prices_df.columns:
                        price_dict = pd.Series(new_prices_df['average'].fillna(0.0).values, index=new_prices_df['resource']).to_dict()
                    elif 'buy' in new_prices_df.columns:
                        price_dict = pd.Series(new_prices_df['buy'].fillna(0.0).values, index=new_prices_df['resource']).to_dict()
                    elif 'price' in new_prices_df.columns:
                        price_dict = pd.Series(new_prices_df['price'].fillna(0.0).values, index=new_prices_df['resource']).to_dict()
                    price_service.update_multiple_prices(price_dict)
                    price_service.save_prices()
                    st.success("Imported CSV into DB and updated current prices.")
                    st.rerun()
                else:
                    if "resource" in new_prices_df.columns and "price" in new_prices_df.columns:
                        price_dict = pd.Series(new_prices_df.price.values, index=new_prices_df.resource).to_dict()
                        price_service.update_multiple_prices(price_dict)
                        price_service.save_prices()
                        st.success("Imported CSV and updated current prices.")
                        st.rerun()
                    else:
                        st.error("Invalid CSV format. Expected 'resource' and 'price' columns.")
            except Exception as e:
                st.error(f"An error occurred during import: {e}")

        # Load from Saved (file backend only)
        if settings.DATA_BACKEND != "sql":
            imports_dir = os.path.join(settings.DATA_ROOT, "user_data", username, "price_imports")
            saved_imports = [f for f in os.listdir(imports_dir) if f.endswith(".csv")] if os.path.isdir(imports_dir) else []
            if saved_imports:
                selected_import = st.selectbox("Or load a saved file to set as default:", options=["-"] + saved_imports)
                if selected_import != "-":
                    if st.button(f"Load: {selected_import}"):
                        try:
                            file_path = os.path.join(imports_dir, selected_import)
                            imported_df = pd.read_csv(file_path)
                            if "resource" in imported_df.columns and "price" in imported_df.columns:
                                price_dict = pd.Series(imported_df.price.values, index=imported_df.resource).to_dict()
                                price_service.update_multiple_prices(price_dict)
                                price_service.save_prices()
                                st.success(f"Successfully set {selected_import} as default prices.")
                                st.rerun()
                            else:
                                st.error("Invalid CSV format in the selected file.")
                        except Exception as e:
                            st.error(f"An error occurred while loading the file: {e}")

        st.divider()

        # --- Bottom Section: Edit Individual Prices in 3 columns ---
        st.subheader("Edit Individual Prices")
        all_prices = price_service.get_all_prices()
        
        if not all_prices:
            st.warning("No prices found. Please import a price file to enable editing.")
        else:
            with st.form("edit_prices_form"):
                updated_prices = {}
                sorted_resources = sorted(all_prices.keys())
                
                cols = st.columns(3)
                
                for i, resource_name in enumerate(sorted_resources):
                    with cols[i % 3]:
                        price = all_prices.get(resource_name, 0.0)
                        updated_prices[resource_name] = st.number_input(
                            label=resource_name,
                            value=float(price),
                            format="%.2f",
                            key=f"price_{resource_name}"
                        )
                
                submitted = st.form_submit_button("Save Edited Prices as Default")
                if submitted:
                    price_service.update_multiple_prices(updated_prices)
                    price_service.save_prices()
                    price_service.load_prices()  # Przeładuj ceny z pliku
                    st.success("Prices saved successfully as default!")
                    st.rerun()

        st.divider()
        st.subheader("Fetch from API (echoes.mobi)")
        with st.form("fetch_echoes_api_form"):
            api_url = st.text_input("API URL", value="https://echoes.mobi/api")
            fetch = st.form_submit_button("Fetch and Apply Prices", type="primary")
            if fetch:
                try:
                    fetched = price_service.fetch_from_echoes_api(api_url)
                    if fetched:
                        price_service.update_multiple_prices(fetched)
                        price_service.save_prices()
                        st.success(f"Fetched {len(fetched)} prices from API and saved.")
                        st.rerun()
                    else:
                        st.warning("No prices parsed from the provided API.")
                except Exception as e:
                    st.error(f"Failed to fetch prices: {e}")

    with tab3:
        st.header("POS Fuel Planner")
        st.info("Wprowadź magazyny paliwa i zużycie/h dla każdego POS, aby obliczyć czas pracy.")

        fuels = [
            {"Fuel": "Heavy Water", "Energy (GJ)": 2},
            {"Fuel": "Suspended Plasma", "Energy (GJ)": 5},
            {"Fuel": "Liquid Ozone", "Energy (GJ)": 13},
            {"Fuel": "Ionic Solutions", "Energy (GJ)": 37},
            {"Fuel": "Oxygen Isotopes", "Energy (GJ)": 83},
            {"Fuel": "Plasmoids", "Energy (GJ)": 191},
        ]

        # Load planner state
        planner = st.session_state.user_prefs.get('pos_planner', {})
        num_pos = int(planner.get('num_pos', 1))
        num_pos = st.number_input("Number of POS", min_value=1, max_value=10, value=num_pos, step=1, key='pos_num')

        # Build editable table (only storage per fuel; usage is total GJ/h per POS)
        import copy
        base_rows = copy.deepcopy(fuels)
        for i in range(1, num_pos + 1):
            storage_key = f"POS {i} Storage (units)"
            for row in base_rows:
                row.setdefault(storage_key, 0)

        # Restore from prefs if shapes match
        saved_rows = planner.get('rows')
        if isinstance(saved_rows, list):
            try:
                # Map by Fuel name and copy known columns
                map_saved = {r.get('Fuel'): r for r in saved_rows}
                for row in base_rows:
                    s = map_saved.get(row['Fuel'])
                    if not s:
                        continue
                    for k in list(row.keys()):
                        if k in s:
                            row[k] = s[k]
            except Exception:
                pass

        df_planner = pd.DataFrame(base_rows)
        # Column config: Energy read-only, but show nicely
        col_cfg = {
            "Energy (GJ)": st.column_config.NumberColumn(disabled=True, format="%d"),
        }
        for i in range(1, num_pos + 1):
            col_cfg[f"POS {i} Storage (units)"] = st.column_config.NumberColumn(min_value=0, step=1, format="%d")

        edited = st.data_editor(
            df_planner,
            column_config=col_cfg,
            use_container_width=True,
            hide_index=True,
            key="pos_planner_editor",
        )

        # Total consumption inputs (GJ/h) per POS
        st.subheader("Consumption (GJ/h)")
        cons_cols = st.columns(min(num_pos, 4)) if num_pos > 1 else st.columns(1)
        consumptions = []
        for i in range(1, num_pos + 1):
            default_val = float(planner.get(f'pos_{i}_consumption_gjh', 18000))
            col = cons_cols[(i-1) % len(cons_cols)]
            val = col.number_input(f"POS {i}", min_value=0.0, value=default_val, step=1.0, key=f"pos_{i}_cons_gjh")
            consumptions.append(val)

        # Compute runtimes per POS based on total stored energy and consumption
        st.divider()
        cols = st.columns(min(num_pos, 3)) if num_pos > 1 else st.columns(1)

        def _calc_energy_gj(df, idx):
            storage_col = f"POS {idx} Storage (units)"
            total_gj = 0.0
            for _, r in df.iterrows():
                units = float(r.get(storage_col, 0) or 0)
                energy_per_unit = float(r.get("Energy (GJ)") or 0)
                total_gj += units * energy_per_unit
            return total_gj

        for i in range(1, num_pos + 1):
            total_energy = _calc_energy_gj(edited, i)
            cons = float(consumptions[i-1] or 0)
            hours = (total_energy / cons) if cons > 0 else 0.0
            days = hours / 24.0
            col = cols[(i-1) % len(cols)]
            col.metric(f"POS {i} Stored Energy", f"{total_energy:,.0f} GJ")
            col.metric(f"POS {i} Runtime", f"{days:,.2f} days", help=f"≈ {hours:,.1f} h")

        # Save planner state
        if st.button("Save POS Planner", use_container_width=True):
            st.session_state.user_prefs['pos_planner'] = {
                'num_pos': int(num_pos),
                'rows': edited.to_dict(orient='records'),
                **{f'pos_{i}_consumption_gjh': float(consumptions[i-1] or 0) for i in range(1, num_pos + 1)}
            }
            save_prefs()
            st.success("Saved POS planner settings.")



if st.session_state.authentication_status:
    main_app()
else:
    login_form()
    with st.expander("🔐 Don't have an account? Register here"):
        registration_form() 