from selenium.webdriver.remote.webdriver import WebDriver


class BasePage(object):

    def __init__(self, driver):
        """

        :param WebDriver driver: The browser's driver:
        """
        self.driver = driver
