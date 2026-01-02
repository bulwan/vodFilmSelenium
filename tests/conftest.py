import os
import time
from datetime import datetime

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()


@pytest.fixture(scope="function")
def setup(request):
    if os.getenv('CI'):
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36"
        )
        options.add_argument("--lang=pl-PL")
    if not os.getenv('CI'):
        options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    request.node.driver = driver
    driver.get("https://vod.film/")
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if any(mark.name == "ui" for mark in item.own_markers):
        if rep.failed and rep.when in ("setup", "call"):
            driver = getattr(item, "driver", None)
            if driver:
                os.makedirs("teardowns", exist_ok=True)
                time.sleep(1)
                file_name = f'{item.originalname}_{datetime.today().strftime("%Y-%m-%d_%H-%M-%S")}.png'.replace(
                    "/",
                    "_").replace(
                    "::", "__")
                file_path = os.path.join("teardowns", file_name)
                driver.save_screenshot(file_path)
