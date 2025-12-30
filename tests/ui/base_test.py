import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup():
    driver = webdriver.Chrome()
    driver.get("https://vod.film/")
    driver.maximize_window()
    yield driver
    if hasattr(driver, "_test_failed"):
        driver.save_screenshot("screenshots/test_failed.png")
    driver.quit()
