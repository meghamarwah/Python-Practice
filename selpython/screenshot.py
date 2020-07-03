from selenium import webdriver
import csv
import pandas as pd
import selenium.webdriver.common.keys

driver = webdriver.Firefox(executable_path="C://Users//Megha//Desktop//geckodriver.exe")
webdriver.driver.get('https://www.flipkart.com')

email=''
password=''
filename='C://Users//Megha//Desktop//Flipkart//data.csv'
# In python the with keyword is used for unmanaged resources (like file streams). 
# It allows you to ensure that a resource is "cleaned up" when the code that uses it finishes running, even if exceptions are thrown.
with open(filename,'r') as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        email = row[0]
        password = row[1]

driver.find_element_by_class_name('_1dBPDZ').send_keys(email)

driver.find_element_by_class_name('_3v41xv').send_keys(password)





driver.get_screenshot_as_file('C://Users//Megha//Desktop//Flipkart//a.png')


