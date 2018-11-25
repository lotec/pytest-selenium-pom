from .base_page import BasePage
from locators.home_page_locators import HomePageLocators
import time


class HomePage(BasePage):

    def load_home_page(self):
        self.driver.get("https://bandcamp.com/")

    def click_gift_page_link(self):
        gift_cards_link = self.driver.find_element(*HomePageLocators.GIFT_CARDS_LINK)
        gift_cards_link.click()

    def register_new_account(self, email, password, username):
        sign_up_link = self.driver.find_element(*HomePageLocators.SIGN_UP_LINK)
        sign_up_link.click()

        fan_signup_link = self.driver.find_element(*HomePageLocators.FAN_SIGNUP_LINK)
        fan_signup_link.click()

        email_field = self.driver.find_element(*HomePageLocators.EMAIL_INPUT)
        email_field.clear()
        email_field.send_keys(email)

        pw = self.driver.find_element(*HomePageLocators.PW_INPUT)
        pw.clear()
        pw.send_keys(password)

        username_field = self.driver.find_element(*HomePageLocators.USERNAME_INPUT)
        username_field.clear()
        username_field.send_keys(username)

        tos = self.driver.find_element(*HomePageLocators.TOS_INPUT)
        tos.click()

        signup_button = self.driver.find_element(*HomePageLocators.SIGNUP_BUTTON)
        signup_button.click()

        time.sleep(7)
