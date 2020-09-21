"""
Start page
"""
import logging
from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class GoogleSearchLocators():
    """
    Start page locators
    """
    GOOGLE_SEARCH_FIELD = (By.NAME, "q")
    GOOGLE_SEARCH_RESULT_ITEM = (By.XPATH, "//div[@class='r']/a")


class StartPage(BasePage):
    """
    Start page
    """

    def enter_word(self, word):
        """
        Enter text into search field
        :param word: word to search
        :return: search_field
        """
        logging.info("Fill search field with word: '%s'", str(word))
        search_field = self.find_element(GoogleSearchLocators.GOOGLE_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        search_field.submit()
        return search_field

    def check_search_results(self, word):
        """
        Verify search
        :param word: word to search
        :return: assert result
        """
        search_result = self.find_elements(GoogleSearchLocators.GOOGLE_SEARCH_RESULT_ITEM, time=10)
        logging.info("Verify is the result of search displayed")
        assert len(search_result) > 0
        logging.info("Verify is the result contain '%s'", str(word))
        for result in search_result:
            title_text = result.find_element_by_tag_name('h3').text
            # print(title_text)
            title_text = title_text.lower()
            logging.info("Checking the following: '%s'", title_text)
            assert word.lower() in title_text
