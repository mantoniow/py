from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_page_load(browser):
    wait = WebDriverWait(browser, 15)
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "*")))

