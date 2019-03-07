from selenium import webdriver

from page import DouMainPage, SearchResultPage

driver = webdriver.Chrome()


def setup_module(module):
    driver.implicitly_wait(5)


def teardown_module(module):
    driver.quit()


base_url = 'https://dou.ua/'
COMPANY_NAME = 'DOU'
INVALID_NAME = '123efdvdfbgfdbfg'


def test_search():
    """Searches for company name, then asserts that name is present in search results """
    main_page = DouMainPage(driver, base_url).open()
    main_page.search_for(COMPANY_NAME)
    result_page = SearchResultPage(driver)
    result_page.assert_result_found(COMPANY_NAME)


def test_invalid_search():
    """Searches for company that don't exists, that asserts that nothing was found"""
    main_page = DouMainPage(driver, base_url).open()
    main_page.search_for(INVALID_NAME)
    result_page = SearchResultPage(driver)
    result_page.assert_no_result_found()
