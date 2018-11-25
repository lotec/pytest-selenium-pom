import random
import string
import time
import datetime
from selenium.common.exceptions import ElementNotVisibleException, \
    TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def random_letters_string(length):
    """Function return a random name
       :param length:  random name string length.
       :type length: int

    """
    random_str = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(length))
    return random_str


def random_string(length):
    """ Function return a random string.
        :param length: random string length.
        :type length: int

    """
    random_str = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))
    return random_str


def get_browser_name(driver):
    current_browser = driver.desired_capabilities['browserName']
    return current_browser


def wait_element(driver, locator_type, locator_value):
    """An expectation for checking that an element is present on the DOM
    of a page and wait for specified time interval. This does not necessarily
    mean that the element is visible.
        :param WebDriver driver: The browser's driver
        :param locator_type: Set of supported locator strategies.
        :type locator_type: Object
        :param locator_value: Value of given locator
        :type locator_value:String
        :return: WebElement object.
    """
    timeout = 15

    try:
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((locator_type, locator_value)))
        return element
    except ElementNotVisibleException:
        driver.quit()


def wait_for_expected_url(driver, expected):
    """
        :param WebDriver driver: The browser's driver
        :param expected:
    """
    timeout = 10
    WebDriverWait(driver, timeout).until(EC.url_contains(expected))


def wait_element_text(driver, text, locator_type, locator_value):
    """An expectation for checking that an element text is present on the DOM
    of a page and wait for specified time interval. This does not necessarily
    mean that the element is visible.
        :param WebDriver driver: The browser's driver
        :param locator_type: Set of supported locator strategies.
        :param locator_value: Value of given locator
        :param text: expected text of element.
        :return: WebElement object.

    """
    timeout = 10
    WebDriverWait(driver, timeout).until(EC.text_to_be_present_in_element((locator_type, locator_value), text))


def scroll_to_element(driver, locator_type, locator_value):
    """
        :param WebDriver driver: The browser's driver
        :param locator_type
        :param locator_value
    """
    element = driver.find_element(locator_type, locator_value)
    driver.execute_script("arguments[0].scrollIntoView();", element)


def scroll_down_once(driver):
    """
        :param WebDriver driver: The browser's driver
    """
    element = driver.find_element_by_tag_name('body')
    element.send_keys('PAGE_DOWN')


def scroll_to_bottom(driver):
    """
        :param WebDriver driver: The browser's driver
    """
    element = driver.find_element_by_tag_name('body')
    element.send_keys(Keys.CONTROL+Keys.END)


def browser_is(driver, browser_name):
    """
        :param WebDriver driver: The browser's driver
        :param browser_name: 'chrome', 'firefox', 'MicrosoftEdge', 'internet explorer', 'safari'
    """
    if driver.desired_capabilities['browserName'] == browser_name:
        return True
    else:
        return False
