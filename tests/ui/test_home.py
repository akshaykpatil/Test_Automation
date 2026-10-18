import pytest
from playwright.sync_api import Page, expect

from framework.config import BASE_URL


@pytest.mark.ui
def test_home_page_loads(page: Page) -> None:
    response = page.goto(BASE_URL, wait_until="domcontentloaded")

    assert response is not None and response.ok
    expect(page).to_have_title(
        "Automation Testing Practice Website for QA and Developers | UI and API"
    )
    expect(page.get_by_role("link", name="Test Login Page")).to_be_visible()
