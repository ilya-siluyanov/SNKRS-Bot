from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from cart_module.cart_api import *
from credentials_module.credentials_api import *
import time

start_time = time.time()
chromeOptions = webdriver.ChromeOptions()

# chromeOptions.add_argument("headless")
# chromeOptions.add_argument("--window-size=200,150")

prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_argument("--start-fullscreen")
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome("drivers/chromedriver", chrome_options=chromeOptions)

link, size = open("links.txt", "r").readlines()[0].split(" ")
link = str(link)
size = str(size)
if size.endswith("\n"):
    temp = size
    size = ""
    for x in temp:
        if x == '\n':
            break
        size += x
middle_time = time.time()
if add_to_cart(driver, link, size):
    print(link, size, "successfully added to the cart")
    go_to_credentials_page(driver)
    fill_credentials(driver)
else:
    print(link, size, "didn't added")
print(time.time() - start_time)
print(time.time() - middle_time)
