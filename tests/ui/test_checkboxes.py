import pytest
from playwright.sync_api import Page, expect

from framework.config import BASE_URL


@pytest.mark.ui
def test_checkbox_defaults_and_toggle(page: Page) -> None:
    response = page.goto(f"{BASE_URL}/checkboxes", wait_until="domcontentloaded")

    assert response is not None and response.ok
    checkbox1 = page.locator("#checkbox1")
    checkbox2 = page.locator("#checkbox2")

    expect(checkbox1).not_to_be_checked()
    expect(checkbox2).to_be_checked()

    checkbox1.check()
    checkbox2.uncheck()

    expect(checkbox1).to_be_checked()
    expect(checkbox2).not_to_be_checked()
