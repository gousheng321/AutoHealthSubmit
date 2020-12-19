# coding=utf-8
import logging
import sys
import time
import os
os.getenv('key_name')

from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException
from selenium import webdriver
from selenium.webdriver.support.select import Select


def login(chrome, usr_name, pwd):
    logger.info("Login for: %s with pass: %s" % (usr_name, pwd))
    chrome.get("https://stuhealth.jnu.edu.cn/#/login")

    element_usr_id = chrome.find_element_by_name('appId')
    element_usr_id.clear()
    element_usr_id.send_keys(usr_name)

    ele_pass = chrome.find_element_by_id('passw')
    ele_pass.clear()
    ele_pass.send_keys(pwd)

    btn = chrome.find_element_by_xpath("//button")
    btn.click()


def submit(chrome):
    logger.info("Start submit")
    # 本人承诺XXX
    ele = chrome.find_element_by_id("10000")
    webdriver.ActionChains(chrome).move_to_element(ele).click(ele).perform()
    # 提交
    ele = chrome.find_element_by_id("tj")
    webdriver.ActionChains(chrome).move_to_element(ele).click(ele).perform()
    

def is_completed(chrome):
    current_page_url = chrome.current_url
    logger.debug(current_page_url)
    return "complete" in current_page_url


def is_logined(chrome):
    current_page_url = chrome.current_url
    logger.debug(current_page_url)
    return "complete" in current_page_url or "index" in current_page_url

driver = webdriver.Chrome('./chromedriver')
driver.set_page_load_timeout(60)
driver.implicitly_wait(10)

usr_id = os.getenv("USERID")
usr_pwd = os.getenv("USERPASS")
completed = False
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    filename="HealthSubmit.log")
logger = logging.getLogger("Health Submit")
ch = logging.StreamHandler()
logger.addHandler(ch)
try:
    login(driver, usr_id, usr_pwd)
    time.sleep(10)
    if(is_logined(driver)):
        if(not is_completed(driver)):
            submit(driver)
        time.sleep(10)
        if(is_completed(driver)):
            completed = True
except Exception as e:
    logger.error("Failed to submit")
driver.quit()
if(completed):
    logger.info("User:%s completed" % usr_id)
else:
    logger.info("User:%s failed" % usr_id)
assert(completed)
