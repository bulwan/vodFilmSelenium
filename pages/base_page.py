from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def open(self, url):
        self.driver.get(url)

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_elements(*locator)

    def _click(self, locator):
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable(locator))
        self.find(locator).click()

    def click_element(self, element):
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable(element))
        element.click()

    def write(self, locator, text):
        element = self.driver.find_element(*locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text
