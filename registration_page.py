
from selenium import webdriver
from Demo_Tricentis_Framework.pages.base_page import BasePage

class RegistrationPage(BasePage):

    register_link = ("link text","Register")
    gender_radio_btn = ("id", "gender-female")
    first_name = ("id","FirstName")
    last_name = ("id","LastName")
    reg_email = ("id","Email")
    password = ("id","Password")
    confirm_pwd = ("id","ConfirmPassword")
    register_btn = ("id","register-button")

    def click_register(self):
        self.click(self.register_link)

    def click_gender(self):
        self.click(self.gender_radio_btn)

    def enter_first_name(self, first_name):
        self.enter_text(self.first_name, first_name)

    def enter_last_name(self, last_name):
        self.enter_text(self.last_name,last_name)

    def enter_email(self,reg_email):
        self.enter_text(self.reg_email,reg_email)

    def enter_password(self,password):
        self.enter_text(self.password,password)

    def enter_confirm_pwd(self,confirm_pwd):
        self.enter_text(self.confirm_pwd,confirm_pwd)

    def click_register_btn(self):
        self.click(self.register_btn)
