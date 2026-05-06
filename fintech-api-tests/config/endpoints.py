"""
config/endpoints.py
───────────────────
All API endpoint paths defined as constants.
Never hardcode paths inside test files — always import from here.

Usage:
    from config.endpoints import Endpoints
    url = f"{settings.BASE_URL}{Endpoints.AUTH_LOGIN}"
"""


class Endpoints:
    """API endpoint path constants."""

    # ── Authentication ────────────────────────────────────────────────────────
    AUTH_LOGIN = "/auth/login"
    AUTH_LOGOUT = "/auth/logout"
    AUTH_REFRESH = "/auth/refresh"
    AUTH_REGISTER = "/auth/register"

    # ── Users ─────────────────────────────────────────────────────────────────
    USERS_ME = "/users/me"
    USERS_BY_ID = "/users/{user_id}"

    # ── Accounts ──────────────────────────────────────────────────────────────
    ACCOUNTS_LIST = "/accounts"
    ACCOUNTS_CREATE = "/accounts"
    ACCOUNTS_BY_ID = "/accounts/{account_id}"
    ACCOUNTS_BALANCE = "/accounts/{account_id}/balance"

    # ── Transactions ──────────────────────────────────────────────────────────
    TRANSACTIONS_LIST = "/transactions"
    TRANSACTIONS_BY_ID = "/transactions/{transaction_id}"
    TRANSACTIONS_BY_ACCOUNT = "/accounts/{account_id}/transactions"

    # ── Payments ──────────────────────────────────────────────────────────────
    PAYMENTS_INITIATE = "/payments"
    PAYMENTS_BY_ID = "/payments/{payment_id}"
    PAYMENTS_STATUS = "/payments/{payment_id}/status"
    PAYMENTS_CANCEL = "/payments/{payment_id}/cancel"

    # ── Health ────────────────────────────────────────────────────────────────
    HEALTH = "/health"
    HEALTH_READY = "/health/ready"
