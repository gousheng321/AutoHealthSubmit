# coding=utf-8
import logging
import os
import time
from selenium import webdriver


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


def get_chrome_driver():
    from selenium import webdriver
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(options=options)


def save_for_email(message):
    # 保存email内容
    with open("email.txt", 'a+', encoding="utf-8") as email:
        email.write(message + '\n')


driver = get_chrome_driver()
driver.set_page_load_timeout(60)
driver.implicitly_wait(10)

usr_id = os.getenv("USERID")
usr_pwd = os.getenv("USERPASS")
completed = False
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger("Health Submit")
try:
    login(driver, usr_id, usr_pwd)
    time.sleep(10)
    if is_logined(driver):
        if not is_completed(driver):
            submit(driver)
        time.sleep(10)
        if is_completed(driver):
            completed = True
except Exception as e:
    logger.error("Failed to submit" + str(e))
    save_for_email("打卡失败：" + str(e))
driver.quit()
if completed:
    logger.info("User:%s completed" % usr_id)
    save_for_email("%s健康申报---成功---！" % usr_id)
else:
    logger.info("User:%s failed" % usr_id)
    save_for_email("%s健康申报----失败----！" % usr_id)
assert(completed)#If not complete fail action to send a mail
