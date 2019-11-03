#!/usr/bin/env python3
from platform import system
from selenium import webdriver
from selenium.webdriver.support.select import Select

class supreme_bot:
    def __init__(self,driver=None):
        self._mainpage = "https://www.supremenewyork.com/shop/all/"
        self._inventories = ["new","jackets","shirts","tops_sweaters","sweatshirts","pants","shorts","hats","bags"]
        self._attributes = ["order_billing_name","order_email",
        "order_tel","bo","oba3","order_billing_zip",
        "order_billing_city","order_billing_state",
        "cnb","credit_card_month","credit_card_year",
        "vval","icheckbox_minimal",'//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins']

        # Windows and Mac support only
        chrome_options = webdriver.ChromeOptions(); 
        chrome_options.add_experimental_option("excludeSwitches", ['enable-automation']); 
        if driver is None:
            if system() == "Windows":
                self._driver = webdriver.Chrome(r"c:\users\taylor\downloads\chromedriver_win32\chromedriver.exe",options=chrome_options)
            else:
                self._driver = webdriver.Chrome(r"/usr/local/bin/chromedriver",options=chrome_options)
                print(str(type(self._driver)))
                # self._driver = webdriver.Remote("http://localhost:4444/wd/hub", webdriver.DesiredCapabilities.HTMLUNIT.copy())
        else:
            self._driver = driver

    def sendinfo(self,info=None):
        if info is None:
            info = ["Taylor Lee", "taylorclee@hotmail.com",
            "8622502038","123 Fake Street","359", "Austin","TX",
            "5561546557454","11","2022","345"]

        assert len(info) == 12
        for i,att in enumerate(self._attributes):
            self._driver.find_element_by_id(att).send_keys(info[i])
 
        self._driver.find_element_by_class_name("icheckbox_minimal").click()
        self._driver.find_element_by_xpath().click()

    def launch(self,product):
        self._driver.get(self._mainpage+product)

if __name__=="__main__":
    bot = supreme_bot()
    bot.launch("jackets")
    bot.sendinfo()
