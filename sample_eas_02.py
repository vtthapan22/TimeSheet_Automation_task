import xlrd
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from _ast import IsNot
from selenium.webdriver.remote import webelement
import chromedriver_autoinstaller
import selenium.webdriver.support.ui as ui

''' Program to make Automation of Timesheet Week - By - week VPN'''

chromedriver_autoinstaller.install()  #Install the Latest version of chromedriver

driver = webdriver.Chrome() #Launch the driver to start Automation
time.sleep(1)   #wait time to load the page
driver.maximize_window() #Maximize the chrome window

driver.get('https://timecard.in.capgemini.com/'); #Time card URL
time.sleep(15)
#locating the Approve button and clicking the same
myElem = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.LINK_TEXT, 'Adjustment Summary')))
eas = driver.find_element_by_link_text("Adjustment Summary")
if eas is None:
    print("Run the program once again...")
else:
    #Try clicking the approve button. If fails in clicking wait for employee to click
    try:
        eas.click()
    except:
        time.sleep(10)
        eas.click()
        
n = datetime.now().month
print(n)
workbook = xlrd.open_workbook("CC.xlsx")
sheet = workbook.sheet_by_name("CC")

rowCount = sheet.nrows
colCount = sheet.ncols
counter = 2
for i in range(n,0,-1):
    WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_ddlStatus']")))        
    emp_sum = driver.find_element_by_id('ctl00_ContentPlaceHolder1_ddlStatus')
    #WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_ddlStatus']/option[7]"))) 
    opt = Select(emp_sum)
    emp_no=len(opt.options)
    opt.select_by_visible_text('Emp AdjSubmitted')
    WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_ddlMonths']"))) 
    sel = Select(driver.find_element_by_xpath("//select[@name='ctl00$ContentPlaceHolder1$ddlMonths']"))
    sel.select_by_index(i-1)
    print("selected "+str(i-1))
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//input[@type="image"][@src="../images/bt-search.gif"]'))).click()
    time.sleep(5)
    #Finding the menu where the employee names are listed for approval/ finding the table to locate the week records
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//table[@id='ctl00_ContentPlaceHolder1_grvApproveTimecard']//tbody//tr")))
    time.sleep(5)
    #counting the NO.of employees in the list
    rows = driver.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_grvApproveTimecard']//tbody//tr")
    print(rows)
    #count no.of records present on the first page
    n = len(rows)
    print(n)
    if n == 26:
        n=0
    if n>1:
        for j in range(2,n+1):
            WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,'/html/body/form/div[3]/div[4]/div/div[2]/div/table/tbody[2]/tr[4]/td/div/div/table/tbody/tr[{0}]/td/a'.format(str(counter))))).click()
            print("clicked")
            emp_code_webpage = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_lblEmpIDVal']"))).text
            chargable_code_webpage = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_grvApproveTimeCard_ctl02_lblTaskName']"))).text            
            for i in range(1,rowCount):
                emp_code_x = sheet.cell_value(i,0) #for project code use(i,2)
                j = i
                if emp_code_webpage == emp_code_x:
                    cc_code_x = sheet.cell_value(j,4)
                    print(emp_code_webpage,emp_code_x,chargable_code_webpage,cc_code_x)
                    if chargable_code_webpage == cc_code_x or chargable_code_webpage=='Leave Code' or chargable_code_webpage=='PUBLIC HOLIDAY' or chargable_code_webpage=='Privilege Leave' or chargable_code_webpage=='Casual Leave':
                        print("Matched")
                        l = driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_txtCommentsForApproveVal']")
                        l.send_keys("Done")
                        WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_btnApprove"]'))).click()
                        print("approved")
                        break
                    else:
                        back_button = driver.find_element_by_xpath("//*[@id='aspnetForm']/div[3]/div[4]/div/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div[2]/input")
                        driver.execute_script("arguments[0].click();", back_button)
                        counter = counter+1
                        break
    else:
        continue