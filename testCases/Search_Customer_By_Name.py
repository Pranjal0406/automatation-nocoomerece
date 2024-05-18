import pytest
import time
import string
import random

from selenium.webdriver.common.by import By

from PageObjects.Add_Customer_Page import AddCustomers
from PageObjects.LoginScreen import LoginPage
from utilities.Read_properties import ReadConfig
from utilities.customLogger import LogGen
from PageObjects.Search_Customer import SearchCustomer


class Test_TC005_Search_customers_by_name:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUseremail()
    password = ReadConfig.getApplicationPassword()
    logs = LogGen.loggen()


    @pytest.mark.regression
    def test_Search_Customer_By_name(self,setup):
        self.logs.info("**************** Search Customer By Email *********************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        time.sleep(2)
        self.logs.info("**************** Login Successful *************")

        self.logs.info("******************** Start searching the customers ")

        self.addcust = AddCustomers(self.driver)
        self.addcust.clickoncustomermenu()
        time.sleep(2)
        self.addcust.clickoncustomersubmenu()
        time.sleep(3)

        self.logs.info("***************** Now Search Customer by name id ******************** ")

        search_cust = SearchCustomer(self.driver)
        search_cust.first_name("Virat")
        time.sleep(1)
        search_cust.last_name("Kohli")
        time.sleep(3)
        search_cust.click_search()
        time.sleep(5)

        status = search_cust.search_customer_By_Name("Virat Kohli")
        assert True == status
        print("Customer is search by NAME is Successful")
        self.logs.info("******************* Test case Passed Successfully I have find the customer by Name ")

        self.driver.close()





