from selenium.webdriver.common.by import By


class SearchCustomer:
    # add customer Page and search with the existing email or first name and last name

    txt_emailXPATH = "//input[@id='SearchEmail']"
    txt_NameXPATH = "//input[@id='SearchFirstName']"
    txt_LastXPATH = "//input[@id='SearchLastName']"
    txt_SearchButtonXpath = "//button[@id='search-customers']"

    table_XPATH = "//div[@id='customers-grid_wrapper']"
    table_rowsXPATH = "//*[@id='customers-grid']/tbody/tr"
    table_ColumnXPATH = "//*[@id='customers-grid']/tbody/tr//td"

    def __init__(self,driver):
        self.driver = driver

    def email_id(self,email):
        self.driver.find_element(By.XPATH,self.txt_emailXPATH).clear()
        self.driver.find_element(By.XPATH,self.txt_emailXPATH).send_keys(email)

    def first_name(self,name):
        self.driver.find_element(By.XPATH,self.txt_NameXPATH).clear()
        self.driver.find_element(By.XPATH,self.txt_NameXPATH).send_keys(name)

    def last_name(self,lname):
        self.driver.find_element(By.XPATH, self.txt_LastXPATH).clear()
        self.driver.find_element(By.XPATH, self.txt_LastXPATH).send_keys(lname)

    def click_search(self):
        self.driver.find_element(By.XPATH, self.txt_SearchButtonXpath).click()

    def getNo_of_Row_Count(self):
        return len(self.driver.find_elements(By.XPATH,self.table_rowsXPATH))

    def getNo_of_Columns_Count(self):
        return len(self.driver.find_elements(By.XPATH,self.table_ColumnXPATH))

    def search_customer_By_email(self,email):
        flag = False
        for r in range(1,self.getNo_of_Row_Count()+1):
            table = self.driver.find_element(By.XPATH,self.table_XPATH)
            emailid = table.find_element(By.XPATH,"//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def search_customer_By_Name(self,name):
        flag = False
        for r in range(1,self.getNo_of_Row_Count()+1):
            table = self.driver.find_element(By.XPATH,self.table_XPATH)
            name_id = table.find_element(By.XPATH,"//*[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name_id == name:
                flag = True
                break
        return flag











