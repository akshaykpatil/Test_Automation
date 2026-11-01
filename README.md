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

To generate and open a self-contained HTML report:

```powershell
New-Item -ItemType Directory -Force .\test-results | Out-Null
python -m pytest .\tests --html=.\test-results\pytest-report.html --self-contained-html
Invoke-Item .\test-results\pytest-report.html
```

The report includes test results and failure details, and is saved locally in
`test-results\pytest-report.html`.

To watch the browser while UI tests run:

```powershell
$env:HEADLESS = "false"
python -m pytest .\tests -m ui
```

## Repeated batch runs

Double-click `run_tests_loop.bat` to run the full suite repeatedly. Each run
creates a uniquely timestamped, self-contained HTML report and text log under
`test-results\`. The batch waits five seconds between runs; close its window
to stop it. The browser runs in headed (visible) mode. A failing test run is
recorded and does not stop subsequent runs.

To run the batch once for verification:

```powershell
.\run_tests_loop.bat --once
```

The batch uses `.venv\Scripts\python.exe` when the project virtual environment
exists; otherwise, it uses `python` from `PATH`.

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
