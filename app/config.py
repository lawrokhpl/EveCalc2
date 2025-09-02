import os


class Settings:
    """Centralized environment configuration for the app (DB, OAuth, switches)."""

    # Data backend fixed to file (SQL removed)
    DATA_BACKEND: str = "file"

    # Auth backend: "local" (default) or "google"
    AUTH_BACKEND: str = os.getenv("AUTH_BACKEND", "local").lower()

    # Removed DB and OAuth settings (not used)

    # Guest/demo access (no persistence)
    ALLOW_GUEST: bool = os.getenv("ALLOW_GUEST", "true").lower() in ("1", "true", "yes", "on")


settings = Settings()


