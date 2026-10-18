import pytest
from playwright.sync_api import APIRequestContext


@pytest.mark.api
def test_health_check_reports_api_up(api_request: APIRequestContext) -> None:
    response = api_request.get("/api/health-check")

    assert response.status == 200
    assert response.json() == {
        "success": True,
        "status": "UP",
        "message": "API is up!",
    }


@pytest.mark.api
def test_practice_api_root_reports_running(api_request: APIRequestContext) -> None:
    response = api_request.get("/api")

    assert response.status == 200
    assert response.json() == {"ApiMessage": "Practice API is Running"}
