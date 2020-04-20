
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import test_email
from datetime import datetime
import pdb
import sys
import re
from login import *
from order import *

def auto_order():
    #chrome_options = Options()
    #chrome_options.add_argument("--window-size=1920,1080")
    #chrome_options.add_argument("--disable-extensions")
    #chrome_options.add_argument("--proxy-server='direct://'")
    #chrome_options.add_argument("--proxy-bypass-list=*")
    #chrome_options.add_argument("--start-maximized")
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    #chrome_options.add_argument('--disable-dev-shm-usage')
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--ignore-certificate-errors')
    #driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()

    driver = login(driver)

    flag = False
    pre_item_cnt = 0
    while not flag:
        driver, flag, pre_item_cnt = order(driver, pre_item_cnt)

if __name__=='__main__':
    auto_order()
