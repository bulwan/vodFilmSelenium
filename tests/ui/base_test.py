import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def setup():
    driver = webdriver.Chrome()
    driver.get("https://vod.film/")
    driver.maximize_window()
    yield driver
    # driver.quit()
