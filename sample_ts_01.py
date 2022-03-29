import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from _ast import IsNot
from selenium.webdriver.remote import webelement


def decision():        
    import tkinter as tk
    root= tk.Tk()
    canvas1 = tk.Canvas(root, width = 400, height = 300)
    canvas1.pack()
    entry1 = tk.Entry (root) 
    canvas1.create_window(200, 140, window=entry1)
    def getSquareRoot ():  
        global x1
        x1 = entry1.get()  
        label1 = tk.Label(root, text= x1)
        canvas1.create_window(200, 230, window=label1)   
    button1 = tk.Button(text='Get the Square Root', command=getSquareRoot)
    canvas1.create_window(200, 180, window=button1)
    root.mainloop()
    

driver = webdriver.Chrome('C://Users//vthapan//Downloads//chromedriver_win32//chromedriver')  # Optional argument, if not specified will search path.
time.sleep(3)
driver.maximize_window()
driver.get('https://www.google.co.in/');
time.sleep(5)
decision()
print(x1)
if x1 == 1:
    driver.close()
    