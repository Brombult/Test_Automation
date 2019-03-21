from selene.api import *

config.browser_name = 'chrome'


def test_blaze():
    browser.open_url('http://www.blazedemo.com/')
    s(by.name('fromPort')).click()
    s(by.text('Boston')).click()
    s(by.name('toPort')).click()
    s(by.text('Berlin')).click()
    s('input[type="submit"]').click()
    s('.container>h3').should(have.text('Flights from Boston to Berlin:'))
