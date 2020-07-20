from unittest.runner import TextTestRunner
from HtmlTestRunner import runner
import pytest
import pytest_html
from selenium import webdriver
@pytest.fixture()
def megha():
    print('This is megha block!')
    driver = webdriver.Firefox(executable_path='C:/Users/Megha/Documents/Python/Selproject/geckodriver_v25/geckodriver.exe')
    driver.get('https://www.flipkart.com')

def testmethod1(megha):
    print('this is test method1')

def testmethod2(megha):
    print('this is test method2')

pytest.main('')