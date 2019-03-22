from selene.api import *
from selene.driver import SeleneDriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select


def test_blaze():
    config.browser_name = 'chrome'
    browser.open_url('http://www.blazedemo.com/')
    s(by.name('fromPort')).click()
    s(by.text('Boston')).click()
    s(by.name('toPort')).click()
    s(by.text('Berlin')).click()
    s('input[type="submit"]').click()
    s('.container>h3').should(have.text('Flights from Boston to Berlin:'))


def test_blaze_with_explicit_driver():
    """Tried combining Selene and Selenium for better readability and usability"""
    driver = SeleneDriver.wrap(Chrome())
    try:
        driver.get('http://www.blazedemo.com/')
        Select(driver.element(by.name('fromPort'))).select_by_visible_text('Boston')
        Select(driver.element(by.name('toPort'))).select_by_visible_text('Berlin')
        driver.element('input[type="submit"]').click()
        driver.element('.container>h3').should(have.text('Flights from Boston to Berlin:'))
    finally:
        driver.quit()
