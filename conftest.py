import pytest
from selenium import webdriver


BROWSERS = {
    'chrome': {'browserName': 'chrome'},
    # 'firefox': {'browserName': 'firefox'},
}

WEBDRIVER_ENDPOINT = 'http://localhost:4444/wd/hub'


@pytest.fixture(params=BROWSERS.keys(), scope='session', autouse=True)
def driver(request):
    browser = webdriver.Remote(
        command_executor=WEBDRIVER_ENDPOINT,
        desired_capabilities=BROWSERS[request.param]
    )
    browser.implicitly_wait(10)
    yield browser
    browser.quit()