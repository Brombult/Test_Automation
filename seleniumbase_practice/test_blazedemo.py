from seleniumbase import BaseCase
from selenium.webdriver.support.ui import Select


class TestBlazeDemo(BaseCase):
    def test_basic(self):
        self.open('http://www.blazedemo.com/')
        Select(self.driver.find_element_by_name('fromPort')).select_by_visible_text('Boston')
        Select(self.driver.find_element_by_name('toPort')).select_by_visible_text('London')
        self.click('[type="submit"]')
        self.assert_exact_text('Flights from Boston to London: ', 'div.container>h3')
        self.assert_text('Virgin America', 'table.table>tbody')
        self.click('table.table>tbody>tr>td>input')
        self.assert_text('Your flight from Boston to London has been reserved', 'div.container>h2')
        self.update_text('#inputName', 'John Doe')
        self.update_text('#address', '123 Main Street')
        self.update_text('#city', 'Boston')
        self.update_text('#state', 'Massachusetts')
        self.update_text('#zipCode', '12345')
        Select(self.driver.find_element_by_id('cardType')).select_by_visible_text('American Express')
        self.update_text('#creditCardNumber', '123456789101112')
        self.update_text('#creditCardMonth', '6')
        self.update_text('#creditCardYear', '2018')
        self.update_text('#nameOnCard', 'John Doe')
        self.click('[type="submit"]')
        self.assert_text('Thank you for your purchase today!', 'div.container>div>h1')
