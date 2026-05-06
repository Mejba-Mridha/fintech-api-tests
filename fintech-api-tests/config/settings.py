"""
config/settings.py
──────────────────
Central configuration module. Loads values from environment variables
(which are populated from .env locally, or GitHub Secrets in CI).

Usage:
    from config.settings import settings
    print(settings.BASE_URL)
"""

import os
from dotenv import load_dotenv

# Load .env file when running locally. In CI, GitHub Secrets are
# already injected as environment variables — load_dotenv is a no-op.
load_dotenv()


class Settings:
    """Holds all runtime configuration for the test suite."""

    # ── API connection ────────────────────────────────────────────────────────
    BASE_URL: str = os.getenv("BASE_URL", "https://api.example-fintech.com/v1")
    API_KEY: str = os.getenv("API_KEY", "")
    AUTH_TOKEN: str = os.getenv("AUTH_TOKEN", "")

    # ── Test account credentials ──────────────────────────────────────────────
    TEST_USER_EMAIL: str = os.getenv("TEST_USER_EMAIL", "testuser@example.com")
    TEST_USER_PASSWORD: str = os.getenv("TEST_USER_PASSWORD", "")

    # ── Test data ─────────────────────────────────────────────────────────────
    DEFAULT_ACCOUNT_ID: str = os.getenv("DEFAULT_ACCOUNT_ID", "acc_test_000001")
    DEFAULT_CURRENCY: str = os.getenv("DEFAULT_CURRENCY", "USD")

    # ── Environment ───────────────────────────────────────────────────────────
    ENV: str = os.getenv("ENV", "staging")

    # ── Request defaults ──────────────────────────────────────────────────────
    TIMEOUT: int = int(os.getenv("REQUEST_TIMEOUT", "30"))
    MAX_RETRIES: int = 3

    def get_auth_headers(self) -> dict:
        """Returns standard Authorization headers for API requests."""
        return {
            "Authorization": f"Bearer {self.AUTH_TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "x-api-key": self.API_KEY,
        }

    def __repr__(self) -> str:
        return (
            f"Settings(env={self.ENV}, base_url={self.BASE_URL}, "
            f"user={self.TEST_USER_EMAIL})"
        )


# Singleton — import this everywhere
settings = Settings()
