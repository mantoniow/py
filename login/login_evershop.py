import time
from selenium.webdriver.common.by import By
from utilities.wait import wait_for_page_load
def login(browser):

    browser.get("https://demo.evershop.io/")
    wait_for_page_load(browser)

    #SUSCRIBE AND LOGIN
    browser.find_element(By.XPATH,"//a[@href='/account/login']").click()
    browser.find_element(By.XPATH,"//a[contains(text(),'Create an account')]").click()
    browser.find_element(By.XPATH,"//input[@name='full_name']").send_keys('Marco Antonio Wong Chu')
    browser.find_element(By.XPATH,"//input[@name='email']").send_keys('mwong@mail.com')
    browser.find_element(By.XPATH,"//input[@name='password']").send_keys('A123456+')
    browser.find_element(By.XPATH,"//form[@id='loginForm']/div[4]/button").click()
    browser.find_element(By.XPATH,"//a[@href='/account/login']").click()
    browser.find_element(By.XPATH,"// input[@name = 'email']").send_keys('mwong@mail.com')
    browser.find_element(By.XPATH,"//input[@name='password']").send_keys('A123456+')
    browser.find_element(By.XPATH,"//span[contains(.,'SIGN IN')]").click()
    time.sleep(2)

