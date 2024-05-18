import pytest
import time
import string
import random

from selenium.webdriver.common.by import By

from PageObjects.Add_Customer_Page import AddCustomers
from PageObjects.LoginScreen import LoginPage
from utilities.Read_properties import ReadConfig
from utilities.customLogger import LogGen


class Test_TC003_add_customers:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getApplicationUseremail()
    password = ReadConfig.getApplicationPassword()
    logs = LogGen.loggen()  # To generate Logs

    @pytest.mark.sanity
    def test_customer(self, setup):

        self.driver = setup
        if self.add_Customers(self):
            print("test case passed")
        else:
            print("test failed")
    def add_Customers(self, setup):
        self.logs.info("*************** Test case add customers starting **************")
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(5)  # seconds

        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.set_username(self.username)
        self.lp.set_password(self.password)
        self.lp.click_login()

        self.logs.info("**************** Login Successful ****************")

        self.logs.info("***************** Start Adding Customers ****************")

        self.addcust = AddCustomers(self.driver)
        self.addcust.clickoncustomermenu()
        self.addcust.clickoncustomersubmenu()
        self.addcust.clickaddnew()

        self.logs.info("**************** Start adding customer details *********************")
        # Use unique emailid for every costumers dont hardcode that use a random email id for that a user defined function
        self.email = random_generator() + "@gmail.com"
        self.addcust.setemail(self.email)
        self.addcust.setpassword("test123")
        self.addcust.setfirstname("Duke")
        self.addcust.setpassword("Disaster")
        self.addcust.setGender("Female")
        self.addcust.setDOB("10051998")
        self.addcust.companyname("The freelancers ")
        self.addcust.newsletter(["Test store 2"])
        self.addcust.customeroles(["Administrators"])
        time.sleep(3)
        self.addcust.setmanagerofvendor("Vendor 2")
        self.addcust.setadmincontent("I am on my way to use the automation skills")
        self.addcust.clickonsave()

        self.logs.info("************ Saving all customer info *************** ")

        self.logs.info("**************** Add customer details validation started ***************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        print(self.msg)
        r = False
        if "The new customer has been added successfully." in self.msg:
            r = True
        else:
            self.driver.save_screenshot(
                "/Users/pranjalnama/PycharmProjects/nopcommereApp/Screenshots/" + "test_03add_cust.png")
            self.logs.error("********** Add Customers details failed to save")

        self.driver.close()
        self.logs.info("************* Ending Customer Test case TC003")
        return r


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


