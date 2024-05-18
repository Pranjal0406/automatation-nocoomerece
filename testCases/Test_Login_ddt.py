import logging

from selenium import webdriver
import pytest
from PageObjects.LoginScreen import LoginPage
from utilities.Read_properties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilis
import time



class Testlogin_ddt :
    baseURL = ReadConfig.getApplicationURL()
    Path = "/Users/pranjalnama/PycharmProjects/nopcommereApp/TestData/LoginData.xlsx"
    logs = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logs.info("***************  Test Data ddt Login ****************")
        self.logs.info("***************  Verifying test data ddt test case  ******************")

        self.driver = setup
        self.driver.get(self.baseURL)
        # How to call these action methods from pageObject class
        # create one object in page object class then we can accesss
        self.lp = LoginPage(self.driver)
        # These methods can use self.driver(theWebDriverinstance) to perform actions on the webpage, such as finding elements and simulating user interactions.

        self.rows = XLUtilis.getRowCount(self.Path,'Sheet1')
        print("Number of rows in the Excel Sheet ", self.rows)
    # Now understand the logic carefully Write a loop and get data from excel file
        list = []  # Empty List Variable
        for r in range(2,self.rows+1):
            self.usrnme = XLUtilis.ReadData(self.Path,'Sheet1',r,1)
            self.passwrd = XLUtilis.ReadData(self.Path,'Sheet1',r,2)
            self.exp = XLUtilis.ReadData(self.Path,'Sheet1',r,3)

            self.lp.set_username(self.usrnme)
            self.lp.set_password(self.passwrd)
            self.lp.click_login()

            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

        # Another important Validation
        # Now 2 validations are there first we need to check the title and second we need to compare the result with expected value
            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logs.info("Test case Passed")
                    self.lp.click_logut()
                    list.append("Pass")

                elif self.exp == "Fail":
                    self.logs.info("Test case Failed")
                    self.lp.click_logut()
                    list.append("Fail")

            if act_title != exp_title:
                if self.exp == "Pass":
                    self.logs.info("Test case Failed")
                    list.append("Fail")
                elif self.exp == "Fail":
                    self.logs.info("Test case Passed")
                    list.append("Pass")
            # When we say the data driven test case is passed if m list contains all are passed otherwise data driven test case is failed

        if "Fail" not in list:
            self.logs.info("******Login DDT test Case is Passed *********")
            self.driver.close()
            assert True
        else:
            self.logs.info("****** Login ddt Test case is failed ******** ")
            self.driver.close()
            assert False

        self.logs.info("************ End of the data driven Test *************")
        self.logs.info("*********** Completed First datadriven test case ")




















