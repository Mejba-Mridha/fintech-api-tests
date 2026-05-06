"""
tests/conftest.py
─────────────────
Pytest fixtures shared across all test modules.
Fixtures here are automatically available to every test file — no import needed.

Key fixtures:
    api_client   — configured requests.Session with auth headers
    auth_token   — valid Bearer token obtained at session start
    test_account — a pre-created account for tests that need one
    fake         — Faker instance for generating realistic test data
"""

import pytest
import requests
import logging
import allure
from faker import Faker

from config.settings import settings
from config.endpoints import Endpoints

logger = logging.getLogger(__name__)


# ─── Session-scoped fixtures (created once per test run) ─────────────────────

@pytest.fixture(scope="session")
def fake() -> Faker:
    """Faker instance for generating realistic test data."""
    return Faker()


@pytest.fixture(scope="session")
def base_url() -> str:
    """The API base URL from environment config."""
    return settings.BASE_URL


@pytest.fixture(scope="session")
def auth_token(base_url: str) -> str:
    """
    Obtains a valid auth token by logging in once per test session.
    All tests that need authentication use this fixture.
    """
    login_url = f"{base_url}{Endpoints.AUTH_LOGIN}"
    payload = {
        "email": settings.TEST_USER_EMAIL,
        "password": settings.TEST_USER_PASSWORD,
    }

    logger.info(f"Authenticating test user: {settings.TEST_USER_EMAIL}")
    response = requests.post(login_url, json=payload, timeout=settings.TIMEOUT)

    assert response.status_code == 200, (
        f"Login failed — expected 200, got {response.status_code}. "
        f"Response: {response.text}"
    )

    token = response.json().get("access_token") or response.json().get("token")
    assert token, "No token found in login response"
    logger.info("Auth token obtained successfully")
    return token


@pytest.fixture(scope="session")
def api_client(auth_token: str) -> requests.Session:
    """
    A requests.Session pre-configured with:
    - Authorization header
    - Content-Type / Accept headers
    - Default timeout
    Session is reused for all tests (performance), then closed after the run.
    """
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    })
    if settings.API_KEY:
        session.headers["x-api-key"] = settings.API_KEY

    logger.info("API client session created")
    yield session

    session.close()
    logger.info("API client session closed")


# ─── Function-scoped fixtures (fresh per test) ────────────────────────────────

@pytest.fixture(scope="function")
def new_user_payload(fake: Faker) -> dict:
    """Generates a unique user registration payload for each test."""
    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.unique.email(),
        "password": "Test@Password123!",
        "phone": fake.numerify("+1##########"),
    }


@pytest.fixture(scope="function")
def payment_payload(fake: Faker) -> dict:
    """Generates a realistic payment request payload."""
    return {
        "amount": round(fake.pyfloat(min_value=1.0, max_value=999.99, right_digits=2), 2),
        "currency": settings.DEFAULT_CURRENCY,
        "source_account_id": settings.DEFAULT_ACCOUNT_ID,
        "destination_account_id": f"acc_dest_{fake.numerify('######')}",
        "description": fake.sentence(nb_words=4),
        "reference": fake.uuid4(),
    }


# ─── Hooks ────────────────────────────────────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Attach response details to Allure report on test failure."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        allure.attach(
            str(item.funcargs),
            name="Test fixtures snapshot",
            attachment_type=allure.attachment_type.TEXT,
        )
