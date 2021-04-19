from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import undetected_chromedriver as uc
from random import randint
import time


opts = Options()
opts.headless = True
assert opts.headless

browser = Firefox(options = opts)
browser.get("https://rocket-league.com/trades/" + input('Insert your nickname: '))
time.sleep(2)
browser.find_element_by_id("acceptPrivacyPolicy").click()
login = browser.find_element_by_id("header-email")
login.clear()
login.send_keys(input('Insert your login: '))

time.sleep(1)

password = browser.find_element_by_id("header-password")
password.clear()
password.send_keys(input('Insert your password: '))

browser.find_element_by_class_name("rlg-btn-primary").click()

while True:
    time.sleep(2)
    trades = browser.find_elements_by_class_name("rlg-trade__bump")
    for trade in trades:
        trade.click()
        time.sleep(2)
        close_not = browser.find_element_by_class_name("rlg-site-popup__container")
        close_not.click()
        time.sleep(2)
    time.sleep(randint(905, 917))
    browser.refresh()
