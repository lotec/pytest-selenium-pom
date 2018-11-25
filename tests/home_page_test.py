from pages.home_page import HomePage


def test_home_page(driver):

    home_page = HomePage(driver)

    home_page.load_home_page()
    home_page.register_new_account('sasas', 'dasdsdas', 'fsdfsdfsd')
