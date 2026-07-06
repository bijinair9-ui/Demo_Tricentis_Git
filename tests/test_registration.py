import pytest
from selenium import webdriver
from selenium.webdriver import chrome, ChromeOptions
from Demo_Tricentis_Framework.pages.registration_page import RegistrationPage
options = ChromeOptions()
driver = webdriver.Chrome(options=options)

def test_valid_registration(setup_and_teardown):
    rp = RegistrationPage(setup_and_teardown)
    rp.click_register()
    rp.click_gender()
    rp.enter_first_name("Test999999")
    rp.enter_last_name("123")
    rp.enter_email("Test@gmail.com")
    rp.enter_password("Test@132")
    rp.enter_confirm_pwd("Test@132")
    rp.click_register()
    # text_logout = driver.find_element("xpath","//a[text()='Log out']").text
    # assert "Log out" in text_logout,"Password and confirmation password do not match"

def test_invalid_registration(setup_and_teardown):
    rp = RegistrationPage(setup_and_teardown)
    rp.click_register()
    rp.click_gender()
    rp.enter_first_name("Test1")
    rp.enter_last_name("456")
    rp.enter_email("Test1@gmail.com")
    rp.enter_password("Test@132")
    rp.enter_confirm_pwd("Test@143")  #password mismatch
    rp.click_register()
    # text = driver.find_element("xpath","//span[text()='The password and confirmation password do not match.']").text
    # assert "The password and confirmation password do not match." in text,"The password and confirmation password do not match"