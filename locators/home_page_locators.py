from selenium.webdriver.common.by import By


class HomePageLocators:
    GIFT_CARDS_LINK = (By.CSS_SELECTOR, '.gift-cards-link')
    SIGN_UP_LINK = (By.CSS_SELECTOR, '.all-signup-link')
    FAN_SIGNUP_LINK = (By.CSS_SELECTOR, '#signup-vm > ul > li.fan.account > div.description > a')
    EMAIL_INPUT = (By.CSS_SELECTOR, '#email-input')
    PW_INPUT = (By.CSS_SELECTOR, '#password-input')
    USERNAME_INPUT = (By.CSS_SELECTOR, '#username-input')
    TOS_INPUT = (By.CSS_SELECTOR, '#tos-input')
    SIGNUP_BUTTON = (By.CSS_SELECTOR, '#signup-vm > div > div.skinny > div.buttons > button')
