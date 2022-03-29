import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from _ast import IsNot
from selenium.webdriver.remote import webelement

if __name__ == "__main__":
    driver = webdriver.Chrome('C://Users//vthapan//Downloads//chromedriver_win32//chromedriver')
    driver.execute_script("window.promptResponse=prompt('Enter smth','smth')")
    a = driver.execute_script("var win = this.browserbot.getUserWindow(); return win.promptResponse")
    print("got back %s" % a)
    
    