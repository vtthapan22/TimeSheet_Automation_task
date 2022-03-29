import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from _ast import IsNot
from selenium.webdriver.remote import webelement
 
driver = webdriver.Chrome('C://Users//vthapan//Downloads//chromedriver_win32//chromedriver')  # Optional argument, if not specified will search path.
time.sleep(3)
driver.maximize_window()
driver.get('https://timecard.in.capgemini.com/');
time.sleep(15) # Let the user actually see something!
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
    print("hi")
else:
    print("yes")
    approve.click()
time.sleep(4)
webtableout = driver.find_element_by_xpath("//table[@style='width: 98%; border: 0;']//tbody//tr[2]//td[4]")
emp_name = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlEmpName')
opt = Select(emp_name)
print(len(opt.options))
opt.select_by_visible_text('Thapan, V')

WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="image"][@src="../images/bt-search.gif"]'))).click()

time.sleep(10)
#webtableout = driver.find_element_by_xpath("//table[@style='width: 98%; border: 0;']//tbody//tr[4]")
webtable = driver.find_element_by_xpath("//table[@style='width: 98%; border: 0;']//tbody//tr[4]")
rows = webtable.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_grvApproveTimecard']//tbody//tr")
n = len(rows)
for i in range(2,n+1):
    driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_grvApproveTimecard']/tbody/tr['"+str(i)+"']/td/a").click()
#print(approve)
#approve.click()
    time.sleep(3)
    l=driver.find_element_by_xpath("//input[@title='Approve']")
    print(l)
    time.sleep(3)
    driver.find_element_by_xpath("//input[@value='Back']").click()
    print("Done ",i)
#driver.quit()
