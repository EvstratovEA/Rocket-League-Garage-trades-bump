from selenium.webdriver import Firefox, FirefoxProfile
from selenium.webdriver.firefox.options import Options
from random import randint
import time
import threading


headless_mode = Options()
headless_mode.headless = True
assert headless_mode.headless

def trade_bump():
    while True:
        time.sleep(3)
        trades = browser.find_elements_by_class_name("rlg-trade__bump") # find 'Bump' buttons on page
        for trade in trades:
            trade.click()
            time.sleep(3)
            close_notific = browser.find_element_by_class_name("rlg-site-popup__container") # find notification about successful/unsuccessful bumping trade
            close_notific.click()
            time.sleep(3)
        time.sleep(randint(905, 917)) # wait 15 munites for refresh page and bump trade again
        browser.refresh()

ff_profile = FirefoxProfile(r"C:\Users\%user_name%\AppData\Roaming\Mozilla\Firefox\Profiles\%selenium_profile")

browser = Firefox(ff_profile, options = headless_mode) # (executable_path = ) - full path to geckodriver.exe

browser.get("https://rocket-league.com/trades/" + input('Insert your nickname: ')) # or replace to your link trade page

time.sleep(2)

try:
    browser.find_element_by_id("acceptPrivacyPolicy").click()
except:
    pass

try:
    login = browser.find_element_by_id("header-email")
    login.clear()
    login.send_keys(input('Insert your login: ')) # or replace your login

    time.sleep(1)

    password = browser.find_element_by_id("header-password")
    password.clear()
    password.send_keys(input('Insert your password: ')) # or replace your password
    browser.find_element_by_class_name("rlg-btn-primary").click()
except:
    pass

trade_cycle = threading.Thread(target = trade_bump, daemon = True)
trade_cycle.start()

while input("Insert 'exit' for stop bump and exit: ") != 'exit': # waiting cycle for stop script and exit
    break

browser.quit()

time.sleep(2)
print('Script was stop')

exit()