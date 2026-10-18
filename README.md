# Expand Testing Practice Automation

A Python and Playwright test framework for the public [Expand Testing practice
site](https://practice.expandtesting.com/). The suite uses pytest, Playwright's
synchronous Python API, and isolated browser contexts for UI tests. API tests
use Playwright's API request client.

## Setup (Windows PowerShell)

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m playwright install chromium
```

If PowerShell blocks virtual-environment activation, run the commands with
`.venv\Scripts\python.exe` instead of activating the environment.

## Run tests

```powershell
pytest
pytest -m ui
pytest -m api
```

To watch the browser while UI tests run:

```powershell
$env:HEADLESS = "false"
pytest -m ui
```

The target URL can be overridden with `BASE_URL`, for example:

```powershell
$env:BASE_URL = "https://practice.expandtesting.com"
pytest
```

## Starter coverage

- Home page smoke check and navigation link.
- Login succeeds with the site's published practice credentials; invalid
  usernames and passwords show the expected error.
- Checkbox defaults and state changes.
- API health check and practice API root response.

The practice site contains many more independent exercises. Add focused tests
under `tests/ui/` or `tests/api/` as coverage is expanded; keep individual
scenarios isolated and label them with the `ui` or `api` pytest marker.
