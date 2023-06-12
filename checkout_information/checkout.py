import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from utilities.wait import wait_for_page_load

def send_checkout_inf(browser):
    browser.find_element(By.XPATH, "//a[starts-with(text(),'VIEW CART')]").click()
    wait_for_page_load(browser)

    browser.find_element(By.XPATH ,"//span[contains(.,'CHECKOUT')]").click()
    time.sleep(10)

    browser.find_element(By.XPATH ,"//input[@name='address[full_name]']").send_keys("Marco Antonio Wong Chu")
    browser.find_element(By.XPATH ,"//input[@name='address[telephone]']").send_keys("(347) 541-9628")
    browser.find_element(By.XPATH ,"//input[@name='address[address_1]']").send_keys("6700 Inwood Ridge Dr")
    browser.find_element(By.XPATH ,"//input[@name='address[city]']").send_keys("Grand Rapids")
    browser.find_element(By.XPATH ,"//input[@name='address[postcode]']").send_keys("49341")
    time.sleep(1)
    select = Select(browser.find_element(By.ID, 'address[country]'))
    select.select_by_value("US")
    time.sleep(2)
    select = Select(browser.find_element(By.ID, 'address[province]'))
    select.select_by_value("US-MI")
    time.sleep(3)
    browser.find_element(By.XPATH ,"//span[starts-with(text(),'Standard')]").click()
    time.sleep(2)
    browser.find_element(By.XPATH ,"//span[starts-with(text(),'Continue')]").click()
    time.sleep(4)
