from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()


class DouMainPage(BasePage):
    SEARCH_FIELD = (By.ID, 'txtGlobalSearch')
    FORUM_LINK = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(3)')
    FEED_LINK = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(4)')
    SALARIES_LINK = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(5)')
    JOBS_LINK = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(6)')
    CALENDAR_LINK = (By.CSS_SELECTOR, 'header>ul>li:nth-of-type(7)')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get('https://dou.ua/')

    def search_for(self, search_string):
        search_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.SEARCH_FIELD))
        search_field.send_keys(search_string)
        search_field.send_keys(Keys.ENTER)
        return SearchResultPage

    def go_to_forum(self):
        self.driver.find_element(*self.FORUM_LINK).click()
        assert 'https://dou.ua/forums/' in self.driver.current_url
        return ForumPage

    def go_to_feed(self):
        self.driver.find_element(*self.FEED_LINK).click()
        assert 'https://dou.ua/lenta/' in self.driver.current_url
        return FeedPage

    def go_to_salaries(self):
        self.driver.find_element(*self.SALARIES_LINK).click()
        assert 'https://jobs.dou.ua/salaries/' in self.driver.current_url
        return SalariesPage

    def go_to_jobs(self):
        self.driver.find_element(*self.JOBS_LINK).click()
        assert 'https://jobs.dou.ua/' in self.driver.current_url
        return JobsPage

    def go_to_calendar(self):
        self.driver.find_element(*self.CALENDAR_LINK).click()
        assert 'https://dou.ua/calendar/' in self.driver.current_url
        return CalendarPage


class SearchResultPage(BasePage):
    CUSTOMER_SEARCH_FIELD = (By.NAME, 'search')
    SEARCH_RESULT_VALID = (By.CLASS_NAME, 'gs-title')
    SEARCH_RESULT_INVALID = (By.CLASS_NAME, 'gs-no-results-result')

    def __init__(self, driver):
        super().__init__(driver)

    def search_for(self, search_string):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(SearchResultPage.CUSTOMER_SEARCH_FIELD)
        ).send_keys(search_string).send_keys(Keys.ENTER)

    def assert_result_found(self, search_string):
        result = self.driver.find_element(*SearchResultPage.SEARCH_RESULT_VALID)
        assert search_string.lower() in result.text.lower()

    def assert_no_result_found(self):
        result = self.driver.find_element(*SearchResultPage.SEARCH_RESULT_INVALID)
        assert 'Результатов нет' in result.text


class ForumPage(BasePage):
    FORUM_TOPIC_SELECTOR = (By.NAME, 'topic')
    PINNED_TOPIC = (By.CSS_SELECTOR, 'article.pinned>h2>a')

    def check_topic_selector(self):
        topic_select = Select(self.driver.find_element(*self.FORUM_TOPIC_SELECTOR))
        topic_select.select_by_index(1)
        assert 'Telegram-канал для IT-спільноти Києва' in self.driver.find_element(*self.PINNED_TOPIC).text


class FeedPage(BasePage):
    SPECIAL_PROJECTS_TABLE = (By.CSS_SELECTOR, 'div.b-similar>ul')

    def check_special_projects(self, projects):
        special_projects = self.driver.find_element(*self.SPECIAL_PROJECTS_TABLE)
        for project in projects:
            assert project in special_projects.text


class SalariesPage(BasePage):
    PERIOD_SELECTOR = (By.NAME, 'period')
    POSITION_SELECTOR = (By.CLASS_NAME, 'salarydec-field-title')
    SPECIALISATION_SELECTOR = (By.NAME, 'spec')
    MIN_SALARY = (By.CSS_SELECTOR, '.salarydec-results-min>.num')

    def check_salaries_widget(self, period_value, position_value, specialisation_value, min_salary):
        period = Select(self.driver.find_element(*self.PERIOD_SELECTOR))
        period.select_by_value(period_value)
        position = Select(self.driver.find_element(*self.POSITION_SELECTOR))
        position.select_by_visible_text(position_value)
        specialisation = Select(self.driver.find_element(*self.SPECIALISATION_SELECTOR))
        specialisation.select_by_visible_text(specialisation_value)
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.MIN_SALARY, min_salary))


class JobsPage(BasePage):
    QA = (By.LINK_TEXT, 'QA')
    KYIV_CITY = (By.CSS_SELECTOR, '.other>li>a')
    JOBS_HEADER = (By.CLASS_NAME, 'b-inner-page-header')

    def go_to_category(self, category):
        self.driver.find_element(By.LINK_TEXT, category).click()

    def go_to_city(self, city):
        self.driver.find_element(By.LINK_TEXT, city).click()
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(self.JOBS_HEADER, city))


class CalendarPage(BasePage):
    CALENDAR_ARCHIVE = (By.CSS_SELECTOR, '.wrap>a')
    CITY_NAME = (By.CSS_SELECTOR, '.b-similar>ul>.item:nth-of-type(5)>.title>.link')
    CITY_SELECTOR = (By.NAME, 'city')
    TOPIC_SELECTOR = (By.NAME, 'tag')

    def check_archive(self, category, city, ):
        self.driver.find_element(*self.CALENDAR_ARCHIVE).click()
        Select(self.driver.find_element(*self.CITY_SELECTOR)).select_by_visible_text(city)
        Select(self.driver.find_element(*self.TOPIC_SELECTOR)).select_by_visible_text(category)
        assert category, city in self.driver.current_url
