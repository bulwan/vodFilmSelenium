import pytest

from pages.search_page import SearchPage


@pytest.mark.parametrize("search_text, should_find_results", [
    ("The pickup", True),
    ("abcxyz123", False),
])
@pytest.mark.ui
def test_search_positive(setup, search_text, should_find_results):
    driver = setup
    page = SearchPage(driver)
    page.close_cookies()
    page.click_search_icon()
    page.search(search_text)
    if should_find_results:
        assert page.is_text_present(search_text)
        page.open_first_result()
        assert page.is_title_visible(search_text)
        assert page.is_player_visible()
        page.play_video()
        page.wait_for_popup()
        before_url, actual_url = page.click_popup_button_and_check_new_url()
        assert before_url != actual_url
    else:
        assert page.is_no_results_present()
