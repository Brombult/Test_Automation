from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_FIELD = (By.ID, 'txtGlobalSearch')
    CUSTOMER_SEARCH_FIELD = (By.NAME, 'search')
    FORUM_LINK = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(3)')
    FEED_LINK = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(4)')
    SALARIES_LINK = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(5)')
    JOBS_LINK = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(6)')
    CALENDAR_LINK = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(7)')
    SEARCH_RESULT_VALID = (By.CLASS_NAME, 'gs-title')
    SEARCH_RESULT_INVALID = (By.CLASS_NAME, 'gs-no-results-result')


class ForumLocators:
    FORUM_TOPIC_SELECTOR = (By.NAME, 'topic')
    PINNED_TOPIC = (By.CSS_SELECTOR, 'article.pinned>h2>a')


class FeedLocators:
    SPECIAL_PROJECTS_TABLE = (By.CSS_SELECTOR, 'div.b-similar>ul')


class SalariesPageLocators:
    PERIOD_SELECTOR = (By.NAME, 'period')
    POSITION_SELECTOR = (By.CLASS_NAME, 'salarydec-field-title')
    SPECIALISATION_SELECTOR = (By.NAME, 'spec')
    MIN_SALARY = (By.CSS_SELECTOR, '.salarydec-results-min>.num')


class JobsPageLocators:
    QA = (By.LINK_TEXT, 'QA')
    KYIV_CITY = (By.CSS_SELECTOR, '.other>li>a')
    JOBS_HEADER = (By.CLASS_NAME, 'b-inner-page-header')


class CalendarLocators:
    CALENDAR_ARCHIVE = (By.CSS_SELECTOR, '.wrap>a')
    CITY_NAME = (By.CSS_SELECTOR, '.b-similar>ul>.item:nth-of-type(5)>.title>.link')
    CITY_SELECTOR = (By.NAME, 'city')
    TOPIC_SELECTOR = (By.NAME, 'tag')
