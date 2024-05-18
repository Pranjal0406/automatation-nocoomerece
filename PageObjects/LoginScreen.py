from selenium .webdriver.common.by import By
from selenium import webdriver
class LoginPage:
    #Capture the locators
    textbox_username_Id = "Email"
    textbox_Password_Id = "Password"
    button_Xpath = "//button[normalize-space()='Log in']"
    # link_text_Logout = "Logout"
    Xpath_logout = "//a[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver = driver


    def set_username(self,username):
        # clear the textbox
        self.driver.find_element(By.ID, self.textbox_username_Id).clear()
        self.driver.find_element(By.ID,self.textbox_username_Id).send_keys(username)

    def set_password(self,password):
        self.driver.find_element(By.ID, self.textbox_Password_Id).clear()
        self.driver.find_element(By.ID, self.textbox_Password_Id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH,self.button_Xpath).click()

    def click_logut(self):
        self.driver.find_element(By.XPATH, self.Xpath_logout).click()


# This is howe design the page object class for login page


