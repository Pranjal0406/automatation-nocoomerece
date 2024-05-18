import logging

from selenium import webdriver
import pytest
from PageObjects.LoginScreen import LoginPage
from utilities.Read_properties import ReadConfig
from utilities.customLogger import LogGen



class Testlogin:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUseremail()
    password = ReadConfig.getApplicationPassword()
    logs = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logs.info("***************  test_homePageTitle  ******************")
        self.logs.info("***************** Verify Home Page title *******************")

        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logs.info("***************** First test case passed  *******************")
        else:
            self.driver.save_screenshot("/Users/pranjalnama/PycharmProjects/nopcommereApp/Screenshots/" + "test_TC1.png")
            self.driver.close()
            self.logs.error("***************** First Test Case Failed  *******************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logs.info("***************  test_Login  ******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        # How to call these action methods from pageObject class
        # create one object in page object class then we can accesss
        self.lp = LoginPage(self.driver)
        # These methods can use self.driver(theWebDriverinstance) to perform actions on the webpage, such as finding elements and simulating user interactions.

        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logs.info("***************** SecondTest Case Passed  *******************")
        else:
            self.driver.save_screenshot("/Users/pranjalnama/PycharmProjects/nopcommereApp/Screenshots/" + "test_TC2.png")
            self.driver.close()
            self.logs.error("***************** Second Test Case Failed  *******************")
            assert False












