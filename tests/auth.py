def test_basic(page):
    page.goto("https://playwright.dev")
    assert "Playwright" in page.title()