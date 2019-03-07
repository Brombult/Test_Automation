from pypom import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DouMainPage(Page):
    _search_field = (By.ID, 'txtGlobalSearch')
    _forum_link = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(3)')
    _feed_link = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(4)')
    _salaries_link = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(5)')
    _jobs_link = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(6)')
    _calendar_link = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(7)')

    def search_for(self, search_string):
        search_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._search_field))
        search_field.send_keys(search_string)
        search_field.send_keys(Keys.ENTER)
        return SearchResultPage


class SearchResultPage(Page):
    URL_TEMPLATE = '/search/'
    _customer_search_field = (By.NAME, 'search')
    _search_result_valid = (By.CLASS_NAME, 'gs-title')
    _search_result_invalid = (By.CLASS_NAME, 'gs-no-results-result')

    def search_for(self, search_string):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self._customer_search_field)
        ).send_keys(search_string).send_keys(Keys.ENTER)

    def assert_result_found(self, search_string):
        result = self.driver.find_element(*self._search_result_valid)
        assert search_string.lower() in result.text.lower()

    def assert_no_result_found(self):
        result = self.driver.find_element(*self._search_result_invalid)
        assert 'Результатов нет' in result.text
