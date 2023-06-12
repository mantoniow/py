import random
import time
from selenium.webdriver.common.by import By
from utilities.wait import wait_for_page_load

def select_prd_category_kids(browser):


    browser.find_element(By.XPATH,"//a[contains(@href, '/category/kids')]").click()
    wait_for_page_load(browser)
    browser.find_element(By.XPATH,"//img[@alt='Continental 80 shoes']").click()
    browser.find_element(By.XPATH,"//input[@name='qty']").clear()
    browser.find_element(By.XPATH,"//input[@name='qty']").send_keys(str(random.randint(7,9)))
    browser.find_element(By.XPATH,"//a[contains(text(),'XL')]").click()
    time.sleep(1)
    browser.find_element(By.XPATH,"//a[contains(text(),'Pink')]").click()
    time.sleep(1)
    browser.find_element(By.XPATH,"//button[contains(.,'ADD TO CART')]").click()
    time.sleep(2)
    browser.find_element(By.XPATH,"//a[contains(text(),'Continue Shopping')]").click()
    time.sleep(2)