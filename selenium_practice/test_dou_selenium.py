import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import (MainPageLocators,
                      ForumLocators,
                      FeedLocators,
                      SalariesPageLocators,
                      JobsPageLocators,
                      CalendarLocators, )

COMPANY_NAME = 'DOU'
INVALID_NAME = '123efdvdfbgfdbfg'
PROJECTS = ('DOU Ревизор', 'DOU Проектор', 'DOU Labs', 'DOU Books')

driver = webdriver.Chrome()


@pytest.fixture(scope='module', autouse=True)
def setup_and_teardown():
    driver.implicitly_wait(5)
    driver.get('https://dou.ua/')
    yield
    driver.quit()


def test_search():
    """Searches for company name, then asserts that name is present in search results """
    search = driver.find_element(*MainPageLocators.SEARCH_FIELD)
    search.send_keys(COMPANY_NAME.lower())
    search.send_keys(Keys.ENTER)
    result = driver.find_element(*MainPageLocators.SEARCH_RESULT_VALID)
    assert COMPANY_NAME.lower() in result.text.lower()


def test_invalid_search():
    """Searches for company that don't exists, that asserts that nothing was found"""
    if driver.current_url == f'https://dou.ua/search/?q={COMPANY_NAME.lower()}':  # these lines ensure that
        search = driver.find_element(*MainPageLocators.CUSTOMER_SEARCH_FIELD)     # this test case can
    else:                                                                         # be run both on it's own
        search = driver.find_element(*MainPageLocators.SEARCH_FIELD)              # and bundled with other test cases
    search.clear()
    search.send_keys(INVALID_NAME)
    search.send_keys(Keys.ENTER)
    result = driver.find_element(*MainPageLocators.SEARCH_RESULT_INVALID)
    assert 'Результатов нет' in result.text


def test_forum_topic_selector():
    """Checks that forum link and forum topic selector are working"""
    driver.find_element(*MainPageLocators.FORUM_LINK).click()
    topic_select = Select(driver.find_element(*ForumLocators.FORUM_TOPIC_SELECTOR))
    topic_select.select_by_index(1)
    assert 'Telegram-канал з корисною для початківців інформацією' in driver.find_element(
        *ForumLocators.PINNED_TOPIC).text


def test_feed_special_projects():
    """Checks that feed link works and special projects are present on feed page"""
    driver.find_element(*MainPageLocators.FEED_LINK).click()
    special_projects = driver.find_element(*FeedLocators.SPECIAL_PROJECTS_TABLE)
    for project in PROJECTS:
        assert project in special_projects.text


def test_salary_widget():
    """Checks that salary link works and salary widget is functioning"""
    driver.find_element(*MainPageLocators.SALARIES_LINK).click()
    period = Select(driver.find_element(*SalariesPageLocators.PERIOD_SELECTOR))
    period.select_by_value('dec2018')
    position = Select(driver.find_element(*SalariesPageLocators.POSITION_SELECTOR))
    position.select_by_visible_text('QA engineer')
    spec = Select(driver.find_element(*SalariesPageLocators.SPECIALISATION_SELECTOR))
    spec.select_by_visible_text('Automation QA')
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(SalariesPageLocators.MIN_SALARY, '1500'))


def test_jobs():
    """Checks that salary link works and both category and city selectors are working"""
    driver.find_element(*MainPageLocators.JOBS_LINK).click()
    driver.find_element(*JobsPageLocators.QA).click()
    city = driver.find_element(*JobsPageLocators.KYIV_CITY)
    city_name = city.text  # using city name from page itself to mitigate possible language differences
    city.click()
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(JobsPageLocators.JOBS_HEADER, city_name))


def test_calendar():
    """Checks that calendar link works and city/topic selectors are functioning"""
    driver.find_element(*MainPageLocators.CALENDAR_LINK).click()
    city_name = driver.find_element(
        *CalendarLocators.CITY_NAME).text  # using city name from page itself to mitigate possible language differences
    driver.find_element(*CalendarLocators.CALENDAR_ARCHIVE).click()
    Select(driver.find_element(*CalendarLocators.CITY_SELECTOR)).select_by_visible_text(city_name)
    Select(driver.find_element(*CalendarLocators.TOPIC_SELECTOR)).select_by_visible_text('QA')
    assert 'Конференция Selenium Camp' in driver.page_source
