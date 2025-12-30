import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()


@pytest.fixture(scope="function")
def setup():
    if os.getenv('CI'):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
    if not os.getenv('CI'):
        options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://vod.film/")
    yield driver
    if hasattr(driver, "_test_failed"):
        driver.save_screenshot("screenshots/test_failed.png")
    driver.quit()
