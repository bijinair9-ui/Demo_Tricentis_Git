import pytest
from Demo_Tricentis_Framework.pages.login_page import LoginPage
from Demo_Tricentis_Framework.utilities import read_excel

@pytest.mark.smoke
@pytest.mark.parametrize("username,password", read_excel.get_data())
def test_valid_login(setup_and_teardown, username, password):
    lp = LoginPage(setup_and_teardown)
    lp.click_login()
    lp.enter_email(username)
    lp.enter_password(password)
    lp.click_login_button()


# def test_invalid_login(setup_and_teardown):
#     lp = LoginPage(setup_and_teardown)
#     lp.click_login()
#     lp.enter_email("biji@g.com")
#     lp.enter_password("qweq")
#     lp.click_login_button()