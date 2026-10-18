from collections.abc import Iterator

import pytest
from playwright.sync_api import APIRequestContext, Browser, Page, Playwright, sync_playwright

from framework.config import BASE_URL, HEADLESS


@pytest.fixture(scope="session")
def playwright_instance() -> Iterator[Playwright]:
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Iterator[Browser]:
    browser = playwright_instance.chromium.launch(headless=HEADLESS)
    yield browser
    browser.close()


@pytest.fixture
def page(browser: Browser) -> Iterator[Page]:
    context = browser.new_context()
    page = context.new_page()
    page.set_default_timeout(10_000)
    yield page
    context.close()


@pytest.fixture(scope="session")
def api_request(playwright_instance: Playwright) -> Iterator[APIRequestContext]:
    request = playwright_instance.request.new_context(base_url=BASE_URL)
    yield request
    request.dispose()
