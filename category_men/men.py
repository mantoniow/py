import random
import time
from selenium.webdriver.common.by import By
from utilities.wait import wait_for_page_load
def select_prd_category_men(browser):

    browser.find_element(By.XPATH, "//a[contains(@href,'/category/men')]").click()
    wait_for_page_load(browser)

    browser.find_element(By.XPATH, "//img[@alt='Nmd_r1 shoes']").click()
    browser.find_element(By.XPATH, "//input[@name='qty']").clear()
    browser.find_element(By.XPATH, "//input[@name='qty']").send_keys(str(random.randint(1,3)))
    browser.find_element(By.XPATH, "//a[contains(text(),'X')]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//a[contains(text(),'Black')]").click()
    time.sleep(1)
    browser.find_element(By.XPATH, "//button[contains(.,'ADD TO CART')]").click()
    time.sleep(3)