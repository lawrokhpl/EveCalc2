import os
import json
from app.config import settings


def _get_preferences_path(username: str) -> str:
    return os.path.join(settings.DATA_ROOT, "user_data", username, "preferences.json")


def load_prefs(username: str) -> dict:
    try:
        prefs_path = _get_preferences_path(username)
        os.makedirs(os.path.dirname(prefs_path), exist_ok=True)
        if os.path.exists(prefs_path):
            with open(prefs_path, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception:
        pass
    return {}


def save_prefs(username: str, preferences: dict) -> None:
    try:
        prefs_path = _get_preferences_path(username)
        os.makedirs(os.path.dirname(prefs_path), exist_ok=True)
        with open(prefs_path, 'w', encoding='utf-8') as f:
            json.dump(preferences, f, indent=4, ensure_ascii=False)
    except Exception:
        pass


