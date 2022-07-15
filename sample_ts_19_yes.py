import xlrd
import time 
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

#locating the Approve button and clicking the same
myElem = WebDriverWait(driver, 500).until(EC.presence_of_element_located((By.LINK_TEXT, 'Approve')))
approve = driver.find_element_by_link_text("Approve")
if approve is None:
    print("Run the program once again...")
else:
    #Try clicking the approve button. If fails in clicking wait for employee to click
    try:
        approve.click()
    except:
        time.sleep(10)
        approve.click()

#Finding the menu where the employee names are listed for approval
WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,"//table[@style='width: 98%; border: 0;']//tbody//tr[4]")))

#counting the NO.of employees in the list
rows = driver.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_grvApproveTimecard']//tbody//tr")
n = len(rows) #finding the no.of employees in the list
print(n)
c = 2
workbook = xlrd.open_workbook("CC.xlsx")
sheet = workbook.sheet_by_name("CC")

rowCount = sheet.nrows
colCount = sheet.ncols
#loop to select the employee and do complete the approval
for i in range(2,5*n+1):
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_grvApproveTimecard"]/tbody/tr[{0}]/td/a'.format(str(c))))).click()
    cc = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_grvApproveTimeCard_ctl02_lblTaskName']"))).text
    #print(cc)
    e_code = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='ctl00_ContentPlaceHolder1_lblEmpIDVal']"))).text
    #print(e_code)bg 
    for i in range(1,rowCount):
        emp_code_x = sheet.cell_value(i,0)
        j = i
        #print(i)
        if e_code == emp_code_x:
            cc_code_x = sheet.cell_value(j,4)
            print(e_code,emp_code_x,cc,cc_code_x)
            if cc == cc_code_x or cc=='Leave Code' or cc=='PUBLIC HOLIDAY' or cc=='Privileged Leave' or cc=='Casual Leave':
                print("Matched")
                button = driver.find_element_by_xpath("//*[@id='ctl00_ContentPlaceHolder1_btnApprove']")
                driver.execute_script("arguments[0].click();", button)
                #print(emp_code_x,e_code,cc,cc_code_x)
                #print("Done")
                break
            else:
                back_button = driver.find_element_by_xpath("//*[@id='aspnetForm']/div[3]/div[4]/div/div/table/tbody/tr/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div[2]/input")
                driver.execute_script("arguments[0].click();", back_button)
                c = c+1
                break
