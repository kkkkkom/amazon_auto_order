
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
import pdb
import sys
import re
import test_email
from common import *

def order(driver, pre_item_cnt=0):
    driver.get("https://www.amazon.com")
    time.sleep(5)

    ### click cart
    loop = 1
    while loop:
        try: 
            driver.find_element_by_xpath(f'/html/body/div[1]/header/div/div[1]/div[2]/div/a[6]').click()
            time.sleep(5)
            loop = 0
        except:
            pass

    ### click check out button
    loop = 1
    while loop:
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div[4]/div[1]/div[4]/div/div/div/div[2]/div/div[1]/div/form/div/div/div/span/span/input').click()
            time.sleep(2)
            loop = 0
        except:
            pass

    loop = 1
    while loop:
        try:
            driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div[1]/div[2]/div/div[2]/div/div/span/span/a').click()
            time.sleep(2)
            loop = 0
        except:
            pass
    url = driver.current_url

    while True:
        driver.get(url)
        time.sleep(2)
        ### check at least 5 items
        item_cnt = 0
        milk_cnt = 0
        for i in range(2,10):
            for j in range(1,5):
                try:
                    item = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/span/form/div[{i}]/div[{j}]/div')
                    item_cnt += 1
                    if re.search('Milk', item.text, re.IGNORECASE|re.MULTILINE):
                        milk_cnt += 1
                    #print(f'Item is: {item.text}')
                except:
                    pass
        
        print(f'Item count is {item_cnt}')
        if item_cnt<4:
        #if item_cnt<0:
            print(f'Item count is {item_cnt}, less than 4, skip')
            if item_cnt!=pre_item_cnt:
                ### send email
                test_email.send_mail(f'Amazon item count below 4, please check', driver.current_url)
                pre_item_cnt = item_cnt
            #return driver, False, item_cnt
            continue

        print(f'Milk count is {milk_cnt}')
        if milk_cnt<2:
            print(f'Milk count is {milk_cnt}, less than 2, skip')
            if item_cnt!=pre_item_cnt:
                ### send email
                test_email.send_mail(f'Amazon milk count below 2, please check', driver.current_url)
                pass
            #return driver, False, item_cnt
            continue

        ### select no substitute for all items
        #print(f'Item count is {item_cnt}, proceeding with order')
        #if not driver.find_element_by_name('doNotSubOrder').is_selected():
        #    driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/span/form/div[1]/div[4]/div/span/div/label/i').click()
        #time.sleep(2)

        ### continue
        driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/span/span/span/input').click()
        time.sleep(2)

        ### check available dates
        for i in range(1,10):
            try:
                date = driver.find_element_by_xpath(f'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/ul/li[{i}]/span/span/span/button/div').text
            except:
                continue

            print(f'Checking date: {date}')
            date_trim = date.split('\n')[1]
            print(f'Trimmed date is: {date_trim}')
            #if not re.search('Today', date, re.MULTILINE):
            #    while True:
            #        pass
            if re.search('Not available', date, re.MULTILINE):
                continue
            else:
                ### send email
                test_email.send_mail(f'Found available delivery date: {date_trim}, please check', driver.current_url)
                #while True:
                #    pass

                print(f'Try placeing order')
                ### delivery time
                found = 0
                for ii in range(1,10):
                    if found: break
                    for jj in range(1,10):
                        try:
                            delivery_time = driver.find_element_by_xpath(f'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[1]/div[3]/div[2]/div/div[3]/div[{ii}]/div/ul/li[{jj}]/span/span/div/div[2]/span/span/button/div')
                            try:
                                delivery_time.click()
                                time.sleep(2)
                                found = 1
                                break
                            except:
                                continue
                        except:
                            continue
                        
                ### continue button
                continue_button_delivery_time = driver.find_element_by_xpath(f'/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div[3]/div/span/span/span/input')
                continue_button_delivery_time.click()
                time.sleep(2)

                ### continue button for selecting payment method
                continue_button_payment = driver.find_element_by_xpath(f'/html/body/div[5]/div[1]/div[2]/div[2]/div[4]/div/form/div[3]/div[1]/div[2]/div/div/div/div[1]/span/span/input')
                continue_button_payment.click()
                time.sleep(2)
                
                ### place order button
                button_place_order = driver.find_element_by_xpath(f'/html/body/div[5]/div[1]/div[2]/form/div/div/div/div[2]/div/div[1]/div/div[1]/div/span/span/input')
                button_place_order.click()
                time.sleep(2)
                
                test_email.send_mail(f'Order placed! {date_trim}, {item_cnt} items, please check', driver.current_url)
                return driver, True, item_cnt
        #return driver, False, item_cnt

