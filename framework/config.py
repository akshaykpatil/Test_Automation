import os


BASE_URL = os.getenv("BASE_URL", "https://practice.expandtesting.com").rstrip("/")
HEADLESS = os.getenv("HEADLESS", "true").lower() not in {"0", "false", "no"}
