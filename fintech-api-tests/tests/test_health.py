"""
tests/test_health.py
─────────────────────
Health check smoke tests — these run first on every commit.
If health fails, all other tests are meaningless.
"""

import pytest
import allure
import requests

from config.settings import settings
from config.endpoints import Endpoints


@allure.epic("Fintech API — Smoke Tests")
@allure.feature("Health Check")
class TestHealthCheck:
    """Verifies the API is reachable and healthy before the full suite runs."""

    @allure.story("API liveness")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_health_endpoint_returns_200(self):
        """The /health endpoint must return 200 OK."""
        url = f"{settings.BASE_URL}{Endpoints.HEALTH}"
        response = requests.get(url, timeout=settings.TIMEOUT)

        assert response.status_code == 200, (
            f"Health check failed — status {response.status_code}. "
            f"API may be down."
        )

    @allure.story("API liveness")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    def test_health_response_time_under_500ms(self):
        """Health endpoint must respond within 500 ms."""
        url = f"{settings.BASE_URL}{Endpoints.HEALTH}"
        response = requests.get(url, timeout=settings.TIMEOUT)

        elapsed_ms = response.elapsed.total_seconds() * 1000
        assert elapsed_ms < 500, (
            f"Health endpoint too slow — {elapsed_ms:.0f}ms (threshold: 500ms)"
        )

    @allure.story("API readiness")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    def test_readiness_endpoint(self):
        """The /health/ready endpoint confirms all dependencies are up."""
        url = f"{settings.BASE_URL}{Endpoints.HEALTH_READY}"
        response = requests.get(url, timeout=settings.TIMEOUT)

        assert response.status_code in (200, 204), (
            f"Readiness check failed — status {response.status_code}"
        )

    @allure.story("API content type")
    @pytest.mark.smoke
    def test_health_returns_json(self):
        """Health response must have Content-Type: application/json."""
        url = f"{settings.BASE_URL}{Endpoints.HEALTH}"
        response = requests.get(url, timeout=settings.TIMEOUT)
        content_type = response.headers.get("Content-Type", "")

        assert "application/json" in content_type, (
            f"Expected JSON content type, got: {content_type}"
        )
