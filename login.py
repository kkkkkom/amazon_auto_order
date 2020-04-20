
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import pdb
import sys
import re
import pickle

def login(driver, email=<your email account>, password=<your pass word>):
    driver.get("https://www.amazon.com")
    time.sleep(5)

    for cookie in pickle.load(open("cookies.pkl", "rb")):
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)

    driver.refresh()
    time.sleep(5)
    #while True:
    #    pass

    '''
    driver.find_element_by_xpath(f'/html/body/div[1]/header/div/div[1]/div[2]/div/a[2]').click()
    time.sleep(5)

    driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]').send_keys(email)
    driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input').click()
    time.sleep(5)

    driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[1]/input').send_keys(password)
    driver.find_element_by_xpath(f'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div/form/div/div[2]/span/span/input').click()
    time.sleep(5)
    while True:
        pass
    '''

    print(f'Login successfully')
    return driver
