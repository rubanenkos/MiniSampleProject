"""
Tests for google search main page
"""
import pytest
from Pages.start_page import StartPage


@pytest.mark.search
@pytest.mark.parametrize("key_word", ["python", "wdcerferferf"])
def test_google_search_1(browser, key_word):
    """
    This is to verify the result of search
    :param browser: webdriver
    :param key_word: word for search
    :return: result
    """
    start_page = StartPage(browser)
    a = browser.session_id
    try:
        start_page.go_to_site()
        start_page.enter_word(key_word)
        start_page.check_search_results(key_word)
    except AssertionError:
        browser.get_screenshot_as_file(a + '.png')
        raise
