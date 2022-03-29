import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from _ast import IsNot
from selenium.webdriver.remote import webelement
 
driver = webdriver.Chrome('C://Users//vthapan//Downloads//chromedriver_win32//chromedriver')
time.sleep(3)
driver.maximize_window()
driver.get('https://timecard.in.capgemini.com/');
time.sleep(15) # Let the user actually see something!
#login_button = driver.find_element_by_id("loginButton_0")
try:
    login_button = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'loginButton_0')))
    login_button.click()
#time.sleep(5)  
    myElem = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.ID, 'idToken1')))
    Corp_id = driver.find_element_by_id('idToken1')
    Corp_id.send_keys('vthapan')
    mobilepass = driver.find_element_by_id('idToken2')
    mobilepass.send_keys('')
    approve = WebDriverWait(driver, 35).until(EC.presence_of_element_located((By.LINK_TEXT, 'Approve')))
    #approve = driver.find_element_by_link_text("Approve")
    if approve is None:
        print("Run the program once again...")
    else:
        #print("yes")
        approve.click()
        time.sleep(4)
    webtableout = driver.find_element_by_xpath("//table[@style='width: 98%; border: 0;']//tbody//tr[2]//td[4]")
    emp_name = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlEmpName')
    opt = Select(emp_name)
    emp_no=len(opt.options)
#Select employee one by one to approve the time sheet
    for i in range(1,3):
        opt.select_by_index(i)
    #time.sleep(10)
    #-----Select employee name by user-------
    #opt.select_by_visible_text('Boggala, Mallikarjun')
        WebDriverWait(driver,100).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="image"][@src="../images/bt-search.gif"]'))).click()
        time.sleep(10)
        webtable = driver.find_element_by_xpath("//table[@style='width: 98%; border: 0;']//tbody//tr[4]")
        rows = webtable.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_grvApproveTimecard']//tbody//tr")
    #Count No.of weeks to be approve for a particular employee
        n = len(rows)
    #To approve the time sheet week by week
        for i in range(2,n+1):
            a=driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_grvApproveTimecard']/tbody/tr[2]/td[4]//span")
            x=int(a.text)
            print(x)
            b=driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_grvApproveTimecard']/tbody/tr[2]/td[5]//span")
            y=int(float(b.text))
            print(y)
        #code to check whether the submitted hours are equal to alloted hours or not
            if x == y:
                driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_grvApproveTimecard']/tbody/tr[2]/td/a").click()
                time.sleep(5)
                driver.find_element_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_grvApproveTimeCard']//tr//td//input[@type='radio']").click()
            #print("Radioclicked")
                val=driver.find_element_by_xpath("//*[text()='Billable']")
                if (val) :
                    print("Matched")
                    driver.find_element_by_xpath("//input[@title='Approve']").click()
                    print("Approved")
                    time.sleep(5)
                else:
                    driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_grvApproveTimecard']/tbody/tr[2]/td/a")#.click()
                    driver.find_element_by_xpath("//input[@title='Reject']")
                    print("Rejected")
                    time.sleep(3)
        emp_name = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlEmpName')
        opt = Select(emp_name)
except:
    approve = WebDriverWait(driver, 100).until(EC.presence_of_element_located((By.LINK_TEXT, 'Approve')))
    #approve = driver.find_element_by_link_text("Approve")
    if approve is None:
        print("Run the program once again...")
    else:
        #print("yes")
        approve.click()
