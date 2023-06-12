import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from login import login_evershop
from category_kids import kids
from category_women import women
from category_men import men
from checkout_information import checkout
from payment_method import payment
from utilities import config
def main():

    #CREATE INSTANCE BROWSER
    service = Service(executable_path= config.PATH_CHROME_DRIVER)
    options = Options()
    options.add_argument('ignore-certificate-errors')
    options.add_argument('window-size=1920x1080')
    options.binary_location = config.PATH_CHROME_EXECUTABLE
    browser = webdriver.Chrome(service=service, options=options)

    try:
        #SUSCRIBE AND LOGIN
        login_evershop.login(browser)

        #SELECT PRODUCTS CATEGORY KIDS
        kids.select_prd_category_kids(browser)

        #SELECT PRODUCTS CATEGORY WOMEN
        women.select_prd_category_women(browser)

        #SELECT PRODUCTS CATEGORY MEN
        men.select_prd_category_men(browser)

        #FILL CHECKOUT OR PAYMENT INFORMATION
        checkout.send_checkout_inf(browser)

        #SELECT PAYMENT METHOD
        payment.confirm_payment(browser)

    except Exception as e:
        #Handle exceptions
        print("An unknown exception occurred:", str(e))

if __name__ == '__main__':
    main()


