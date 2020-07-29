from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from cart_module.cart_api import *
from credentials_module.credentials_api import *

chromeOptions = webdriver.ChromeOptions()
#chromeOptions.add_argument("headless")
prefs = {"profile.managed_default_content_settings.images": 2}
chromeOptions.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chromeOptions)


link, size = open("links.txt", "r").readlines()[0].split(" ")
link = str(link)
size = str(size)
if size.endswith("\n"):
    size = size[0:-3]
if add_to_cart(driver, link, size):
    print(link, size, "successfully added")
else:
    print(link, size, "didn't added")

print("GET : https://www.nike.com/ru/ru/cart")
driver.get("https://www.nike.com/ru/ru/cart")

go_to_credentials_page(driver)
fill_credentials(driver)
# driver.close()
