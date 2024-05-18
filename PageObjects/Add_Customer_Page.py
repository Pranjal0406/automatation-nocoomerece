import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class AddCustomers:
    lnk_customer_menu_Xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnk_customer_menu_Sub_Xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    txt_Add_Button = "//a[normalize-space()='Add new']"
    txt_Save_button = "//button[@name='save']"
    Email_Xpath = "//input[@id='Email']"
    Password_Xpath = "//input[@id='Password']"
    First_nme_Xpath = "//input[@id='FirstName']"
    Last_nme_Xpath = "//input[@id='LastName']"
    Male_Click_button_Xpath = "//input[@id='Gender_Male']"
    Female_Click_Button_Xpath = "//input[@id='Gender_Female']"
    Dob_Xpath = "//input[@id='DateOfBirth']"
    Company_name_Xpath = "//input[@id='Company']"
    txtNewsLetter_Xpath = "//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/span/span[1]/span/ul/li/input"
    lstyourstorenme = "/html/body/span/span/span/ul/li[1]" # Customisable XPATH
    lstteststore2 = "/html/body/span/span/span/ul/li[2]" # Customisable Xpath
    Vendor_Xpath = "//select[@id='VendorId']"
    txt_Customers_Roles = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul"
    txt_Administrator_Xpath = "/html/body/span/span/span/ul/li[1]"
    txt_ForumAdministrator_Xpath = "/html/body/span/span/span/ul/li[2]"
    txt_Guests_Xpath = "/html/body/span/span/span/ul/li[4]"
    txt_Register_Xpath = "/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul/li[1]"
    txt_close_Register_Xpath = "//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/span/span[1]/span/ul/li[1]/span"
    txt_Vendors_Xpath = "/html/body/span/span/span/ul/li[5]"
    drpManager_vender = "//select[@id='VendorId']"
    txtAdmin_Content_Xpath = "//textarea[@id='AdminComment']"

    def __init__(self, driver):
        self.driver = driver

    def clickoncustomermenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menu_Xpath).click()

    def clickoncustomersubmenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menu_Sub_Xpath).click()

    def clickaddnew(self):
        self.driver.find_element(By.XPATH, self.txt_Add_Button).click()

    def setemail(self, email):
        self.driver.find_element(By.XPATH, self.Email_Xpath).send_keys(email)

    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.Password_Xpath).send_keys(password)

    def setfirstname(self, name):
        self.driver.find_element(By.XPATH, self.First_nme_Xpath).send_keys(name)

    def setlastname(self, last):
        self.driver.find_element(By.XPATH, self.Last_nme_Xpath).send_keys(last)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH, self.Male_Click_button_Xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.Female_Click_Button_Xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.Male_Click_button_Xpath).click()

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.Dob_Xpath).send_keys(dob)

    def companyname(self, compnme):
        self.driver.find_element(By.XPATH, self.Company_name_Xpath).send_keys(compnme)

    def newsletter(self, list):
        self.driver.find_element(By.XPATH, self.txtNewsLetter_Xpath).click()
        for newsletr in list:
            if newsletr == 'Your store name':
                self.driver.find_element(By.XPATH, self.lstyourstorenme).click()
            elif newsletr == 'Test store 2':
                self.driver.find_element(By.XPATH, self.lstteststore2 ).click()

    def customeroles(self, list1):
        self.driver.find_element(By.XPATH, self.txt_Customers_Roles).click()
        is_Register = False
        is_Guest = False
        for item in list1:
            if item == 'Registered':
                is_Register = True
            if item == 'Guests':
                is_Guest = True

        if is_Register == True and is_Guest == True:
            print("***** Test case failed *****")
            return

        elif is_Guest == True:
            self.driver.find_element(By.XPATH, self.txt_close_Register_Xpath).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.txt_Customers_Roles).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.txt_Guests_Xpath).click()

        for item in list1:

            if item == 'Forum Moderators':
                self.driver.find_element(By.XPATH, self.txt_ForumAdministrator_Xpath).click()
            elif item == 'Vendors':
                self.driver.find_element(By.XPATH, self.txt_Vendors_Xpath).click()
            elif item == 'Administrators':
                self.driver.find_element(By.XPATH, self.txt_Administrator_Xpath).click()

    def setmanagerofvendor(self,value):
        drp = Select(self.driver.find_element(By.XPATH,self.drpManager_vender))
        drp.select_by_visible_text(value)

    def setadmincontent(self,content):
        self.driver.find_element(By.XPATH,self.txtAdmin_Content_Xpath).send_keys(content)

    def clickonsave(self):
        self.driver.find_element(By.XPATH,self.txt_Save_button).click()
