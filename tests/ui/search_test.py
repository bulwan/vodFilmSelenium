from pages.search_page import SearchPage
from tests.ui.base_test import setup


def test_search_positive(setup, search_text="The pickup"):
    driver = setup
    page = SearchPage(driver)
    page.close_cookies()
    page.click_search_icon()
    page.search(search_text)
    assert page.is_text_present(search_text)
    page.open_first_result()
    assert page.is_title_visible(search_text)
    assert page.is_player_visible()
    page.click_play_button()
    page.wait_for_popup()
    page.click_popup_button_and_check_new_url()

def test_search_negative(setup, search_text="abcxyz123"):
    driver = setup
    page = SearchPage(driver)
    page.close_cookies()
    page.click_search_icon()
    page.search(search_text)
    assert page.is_text_present(search_text)
    page.open_first_result()
    assert page.is_title_visible(search_text)
    assert page.is_player_visible()
    page.click_play_button()
    page.wait_for_popup()
    page.click_popup_button_and_check_new_url()
