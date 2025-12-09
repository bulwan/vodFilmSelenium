from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    def open(self, url):
        """Navigate to given url

        Args:
            url (str): target url to open
        """
        self.driver.get(url)

    def find(self, locator):
        """Find single element by locator

        Args:
            locator (tuple): tuple containing locator type and value

        Returns:
            WebElement: The found web element.
        """
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        """Find multiple elements by locator

        Args:
            locator (tuple): tuple containing locator type and value

        Returns:
            WebElement: The found web element.
        """
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable(locator))
        return self.driver.find_elements(*locator)

    def _click(self, locator):
        """Click element by locator

        Args:
            locator (tuple): tuple containing locator type and value
        """
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable(locator))
        self.find(locator).click()

    def click_element(self, element):
        """Click given element

        Args:
            element (WebElement): Web element to click
        """
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable(element))
        element.click()

    def write(self, locator, text):
        """Send given text to given locator
        Args:
            locator (tuple): tuple containing locator type and value
            text (str): text to send
        """
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """Get text from given locator
        Args:
            locator (tuple): tuple containing locator type and value
        Returns:
            str: text from given locator
        """
        element = self.driver.find(*locator)
        return element.text
