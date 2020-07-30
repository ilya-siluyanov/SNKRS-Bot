import time
from selenium.webdriver.common.by import By

SLEEP_TIMEOUT = 0
k = 0
maxPress = 0


def is_cart_empty(cart):
    try:
        cart.find_element_by_tag_name("span")
        return False
    except Exception:
        print("The cart is empty")
        return True


def push_while_not_added(cart, submit):
    sleep_time = 0.2
    while is_cart_empty(cart):
        try:
            submit.click()
            print("An attempt to push the item to the cart")
            time.sleep(sleep_time)
        except Exception:
            print("something is wrong with submit button")
            push_while_not_added(cart, submit)


def get_cart_link(driver):
    return driver.find_element_by_tag_name("ul").find_element(By.XPATH,
                                                              "/html/body/div[@id='root']/div[@class='u-full-width u-full-height']/div[@class='root-controller remove-outline']/div[@class='main-layout']/div[@class='content-wrapper']/header[@class='ncss-col-sm-12']/div[@class='d-lg-h d-sm-b']/section[@class='mobile-top-nav']/div[@class='prl4-sm prl7-lg va-sm-m ta-sm-r']/a[@class='bg-transparent prl3-sm pt4-sm pb4-sm d-sm-b shopping-cart jewel-cart-container']")


def add_to_cart(driver, link, size):
    print("GET : {}".format(link))
    driver.get(link)
    cart = get_cart_link(driver)
    print("The cart found")
    container = driver.find_elements_by_class_name("buying-tools-container")[0]

    found = False
    sizes_container = container.find_element_by_tag_name("ul").find_elements_by_tag_name("li")
    for li in sizes_container:
        button = li.find_element_by_tag_name("button")
        if button.get_attribute("disabled") == "true":
            continue
        row_size = button.text
        real_size = row_size.split(" ")[3][0:-1]
        if real_size == size:
            button.click()
            print("{} size chose".format(real_size))
            found = True
            break
    if not found:
        return False

    submit = container.find_elements_by_tag_name("button")[-1]
    time.sleep(SLEEP_TIMEOUT)
    push_while_not_added(cart, submit)
    # submit.click()
    return True

