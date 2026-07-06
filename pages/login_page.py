from selenium import webdriver

from Demo_Tricentis_Framework.pages.base_page import BasePage

class LoginPage(BasePage):

    login_link=("link text","Log in")
    email = ("id","Email")
    password = ("id","Password")
    login_button = ("xpath","(//input[@type='submit'])[2]")

    def click_login(self):
        self.click(self.login_link)

    def enter_email(self,email):
        self.enter_text(self.email,email)

    def enter_password(self,password):
        self.enter_text(self.password,password)

    def click_login_button(self):
        self.click(self.login_button)

        