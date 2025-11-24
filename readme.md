# Python + Playwright automation (learning / pet project)

Short project README for a learning automation project using Python, pytest and Playwright. Contains quick setup and common commands.

## Purpose
- Learn web UI automation with Playwright and pytest.
- Keep code organised: tests, page objects, and a central config for static values (BASE_URL, timeouts).

## Project layout (example)
- config/settings.py  — central place for BASE_URL and other static settings
- pages/              — Page Objects
- tests/              — pytest test files
- pyproject.toml      — Poetry project config

## Where to keep BASE_URL
- Put static variables like BASE_URL in config/settings.py (export a Config or constants).
- Import Config.BASE_URL in Page Objects and tests instead of hard-coding URLs.
- Example usage: BasePage should accept a path or full URL and build the final URL with Config.BASE_URL.

## Prerequisites
- Python 3.10+ (or as required by your pyproject.toml)
- Poetry (recommended) or pip for dependency management

## Quick setup (Poetry)
1. Install Poetry (official installer or pipx). Example:
   - (Windows PowerShell) (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   - or: pipx install poetry
2. From project root:
   - poetry install
   - If dependencies are not listed yet: poetry add --group dev pytest pytest-playwright playwright

3. Install Playwright browsers:
   - poetry run playwright install

## Running tests
- Run all tests:
  - poetry run pytest
- Run a single test or marker:
  - poetry run pytest tests/test_example.py -q
- To run headed (show browser), set HEADLESS=false in env or adjust Config:  
  - Windows (PowerShell): $env:HEADLESS="false"; poetry run pytest

## Notes
- Keep secrets and environment-specific values out of the repo. Use a .env (read by python-dotenv) or environment variables.
- Use Config (config/settings.py) to centralise static vars (BASE_URL, DEFAULT_TIMEOUT).
- BasePage should use Config.BASE_URL so tests remain environment-agnostic.

## Troubleshooting
- If Playwright complains about missing browsers: run `poetry run playwright install`.
- If tests fail due to timeouts, increase DEFAULT_TIMEOUT in config/settings.py.
