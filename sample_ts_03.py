import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
 
driver = webdriver.Chrome('C://Users//vthapan//Downloads//chromedriver_win32//chromedriver')  # Optional argument, if not specified will search path.
time.sleep(3)
driver.maximize_window()
driver.get('https://timecard.in.capgemini.com/');
time.sleep(10) # Let the user actually see something!
login_button = driver.find_element_by_id("loginButton_0")
myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'loginButton_0')))
login_button.click()
#time.sleep(5)  
myElem = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'idToken1')))
Corp_id = driver.find_element_by_id('idToken1')
Corp_id.send_keys('vthapan')
mobilepass = driver.find_element_by_id('idToken2')
mobilepass.send_keys('')
myElem = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.LINK_TEXT, 'Approve')))
approve = driver.find_element_by_link_text("Approve")
if approve is None:
    print("hi",approve)
else:
    print("yes",approve)
    approve.click()
    