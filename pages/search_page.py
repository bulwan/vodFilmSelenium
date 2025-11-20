from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class SearchPage(BasePage):
    COOKIE_AGREE = (By.XPATH, '//*[@id=\"cookie-banner"]/div/div[3]/button[2]')
    SEARCH_ICON = (By.CSS_SELECTOR, 'img[alt="search icon"]')
    SEARCH_BAR = (By.ID, 'search')
    SEARCH_RESULTS = (By.CLASS_NAME, 'animation-fade-in')
    MATCHED_MOVIE = (By.XPATH, '(//article/p/a)[1]')
    MOVIE_TITLE = (By.TAG_NAME, 'h1')
    VIDEO_PLAYER = (By.TAG_NAME, 'video')
    PLAY_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Play"]')
    POP_UP = (By.ID, 'popup')
    POP_UP_REGISTER_BUTTON = (By.ID, 'register-now')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_search_icon(self):
        self._click(self.SEARCH_ICON)

    def search(self, text):
        self.write(self.SEARCH_BAR, text)

    def is_text_present(self, text):
        # wait = WebDriverWait(self.driver, self.timeout)
        # wait.until(EC.visibility_of_element_located(self.SEARCH_RESULTS))
        sleep(2)
        result = self.find(self.SEARCH_RESULTS)
        return text.lower() in result.text.lower()

    def is_title_visible(self, text):
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.text_to_be_present_in_element(self.MOVIE_TITLE, text.title()))
        return text.lower() in self.find(self.MOVIE_TITLE).text.lower()

    def is_player_visible(self):
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.visibility_of_element_located(self.VIDEO_PLAYER))
        return self.find(self.VIDEO_PLAYER)

    def click_play_button(self):
        wait = WebDriverWait(self.driver, self.timeout)
        wait.until(EC.element_to_be_clickable(self.PLAY_BUTTON))
        play_button = self.find(self.PLAY_BUTTON)
        ActionChains(self.driver).scroll_to_element(play_button).perform()
        self._click(self.PLAY_BUTTON)

    def open_first_result(self):
        self._click(self.MATCHED_MOVIE)

    def close_cookies(self, timeout=10):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable(self.COOKIE_AGREE))
        banner_close = self.find(self.COOKIE_AGREE)
        banner_close.click()

    def wait_for_popup(self):
        wait = WebDriverWait(self.driver, 60)
        wait.until(EC.visibility_of_element_located(self.POP_UP))

    def click_popup_button_and_check_new_url(self):
        current_url = self.driver.current_url
        register_buttons = self.find_elements(self.POP_UP_REGISTER_BUTTON)
        wait = WebDriverWait(self.driver, self.timeout)
        self.click_element(register_buttons[1])
        wait.until(EC.url_changes(current_url))
        new_url = self.driver.current_url
        print(new_url)
