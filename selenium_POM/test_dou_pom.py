from urllib.parse import unquote
from selenium import webdriver

from page import (DouMainPage,
                  SearchResultPage,
                  ForumPage,
                  FeedPage,
                  SalariesPage,
                  JobsPage,
                  CalendarPage, )

COMPANY_NAME = 'DOU'
INVALID_NAME = '123efdvdfbgfdbfg'
PROJECTS = ('DOU Ревизор', 'DOU Проектор', 'DOU Labs', 'DOU Books')

SALARIES_PERIOD_VALUE = 'dec2018'
SALARIES_POSITION_VALUE = 'QA engineer'
SALARIES_SPECIALISATION_VALUE = 'Automation QA'
SALARIES_MIN_SALARY = '1500'

JOB_CATEGORY = 'QA'
JOB_CITY = 'Киев'

CALENDAR_CATEGORY = 'QA'
CALENDAR_CITY = 'Киев'

driver = webdriver.Chrome()


def setup_module(module):
    driver.implicitly_wait(5)


def teardown_module(module):
    driver.quit()


def test_search():
    """Searches for company name, then asserts that name is present in search results """
    main_page = DouMainPage(driver)
    main_page.search_for(COMPANY_NAME)
    result_page = SearchResultPage(driver)
    result_page.assert_result_found(COMPANY_NAME)


def test_invalid_search():
    """Searches for company that don't exists, that asserts that nothing was found"""
    main_page = DouMainPage(driver)
    main_page.search_for(INVALID_NAME)
    result_page = SearchResultPage(driver)
    result_page.assert_no_result_found()


def test_forum_topic_selector():
    """Checks that forum link and forum topic selector are working"""
    main_page = DouMainPage(driver)
    main_page.go_to_forum()
    forum_page = ForumPage(driver)
    forum_page.check_topic_selector()


def test_feed_special_projects():
    """Checks that feed link works and special projects are present on feed page"""
    main_page = DouMainPage(driver)
    main_page.go_to_feed()
    feed_page = FeedPage(driver)
    feed_page.check_special_projects(PROJECTS)


def test_salaries_widget():
    """Checks that salary link works and salary widget is functioning"""
    main_page = DouMainPage(driver)
    main_page.go_to_salaries()
    salaries_page = SalariesPage(driver)
    salaries_page.check_salaries_widget(
        SALARIES_PERIOD_VALUE, SALARIES_POSITION_VALUE, SALARIES_SPECIALISATION_VALUE, SALARIES_MIN_SALARY
    )


def test_jobs_category_and_city():
    """Checks that salary link works and both category and city selectors are working"""
    main_page = DouMainPage(driver)
    main_page.go_to_jobs()
    job_page = JobsPage(driver)
    job_page.go_to_category(JOB_CATEGORY)
    job_page.go_to_city(JOB_CITY)
    assert JOB_CATEGORY and JOB_CITY in unquote(driver.current_url)


def test_calendar_archive():
    """Checks that calendar link works and city/topic selectors are functioning"""
    main_page = DouMainPage(driver)
    main_page.go_to_calendar()
    calendar_page = CalendarPage(driver)
    calendar_page.check_archive(CALENDAR_CATEGORY, CALENDAR_CITY)
