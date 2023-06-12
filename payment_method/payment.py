import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.wait import wait_for_page_load

def confirm_payment(browser):
    browser.find_element(By.CLASS_NAME, 'feather').click()
    wait_for_page_load(browser)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    wait_for_page_load(browser)

    # INSIDE IFRAME PAYMENT METHOD
    WebDriverWait(browser, 5).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, 'iframe')))
    cn = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.XPATH, '//input[@name="cardnumber" and @type="text"]')))
    cn.send_keys("4242424242424242")

    time.sleep(1)
    browser.find_element(By.XPATH, "//input[@name='exp-date']").send_keys("04 / 24")
    time.sleep(1)
    browser.find_element(By.XPATH, "//input[@name='cvc']").send_keys("242")
    time.sleep(2)

    # RETURN TO MAIN PAGE
    browser.switch_to.default_content()

    # SEND ORDER
    browser.find_element(By.XPATH, "//*[contains(text(), 'Place Order')]").click()
    time.sleep(5)
