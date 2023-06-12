import random
import time
from selenium.webdriver.common.by import By
from utilities.wait import wait_for_page_load
def select_prd_category_women(browser):
    browser.find_element(By.XPATH, "//a[contains(@href,'/category/women')]").click()
    wait_for_page_load(browser)
    browser.find_element(By.XPATH, "//img[@alt='Lite racer adapt 3.0 shoes']").click()
    browser.find_element(By.XPATH, "//input[@name='qty']").clear()
    browser.find_element(By.XPATH, "//input[@name='qty']").send_keys(str(random.randint(4,6)))
    browser.find_element(By.XPATH, "//a[contains(text(),'L')]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//a[contains(text(),'White')]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//button[contains(.,'ADD TO CART')]").click()
    time.sleep(2)
    browser.find_element(By.XPATH, "//a[contains(text(),'Continue Shopping')]").click()
    time.sleep(2)
