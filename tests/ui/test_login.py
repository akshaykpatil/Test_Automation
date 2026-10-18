import pytest
from playwright.sync_api import Page, expect

from framework.config import BASE_URL


@pytest.mark.ui
def test_login_with_valid_credentials(page: Page) -> None:
    response = page.goto(f"{BASE_URL}/login", wait_until="domcontentloaded")

    assert response is not None and response.ok
    page.get_by_label("Username").fill("practice")
    page.get_by_label("Password").fill("SuperSecretPassword!")
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(f"{BASE_URL}/secure")
    expect(page.get_by_text("Welcome to the Secure Area.")).to_be_visible()


@pytest.mark.ui
@pytest.mark.parametrize(
    ("username", "password", "error_message"),
    [
        ("wrongUser", "SuperSecretPassword!", "invalid!"),
        ("practice", "wrongPassword", "Your password is invalid!"),
    ],
    ids=["invalid-username", "invalid-password"],
)
def test_login_rejects_invalid_credentials(
    page: Page, username: str, password: str, error_message: str
) -> None:
    response = page.goto(f"{BASE_URL}/login", wait_until="domcontentloaded")

    assert response is not None and response.ok
    page.get_by_label("Username").fill(username)
    page.get_by_label("Password").fill(password)
    page.get_by_role("button", name="Login").click()

    expect(page).to_have_url(f"{BASE_URL}/login")
    expect(page.locator("#flash")).to_be_visible()
    expect(page.locator("#flash")).to_contain_text(error_message)
