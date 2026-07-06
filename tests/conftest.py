import pytest

from selenium import webdriver

@pytest.fixture(params=['chrome','edge','firefox'])
def setup_and_teardown(request):
    parameter = request.param

    if parameter == 'chrome':
        driver = webdriver.Chrome()
    if parameter == 'edge':
        driver = webdriver.Edge()
    if parameter == 'firefox':
        driver = webdriver.Firefox()

    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    yield driver
    driver.quit()