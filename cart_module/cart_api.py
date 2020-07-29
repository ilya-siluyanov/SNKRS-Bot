import time

SLEEP_TIMEOUT = 1
k = 1
maxPress = 1


def is_cart_empty(cart):
    try:
        cart.find_element_by_tag_name("span")
        return False
    except Exception:
        print("The cart is empty")
        return True


def try_to_push(cart, submit):
    submitPressed = 0
    while is_cart_empty(cart):
        try:
            submit.click()
            print("An attempt to push the item to the cart")
            time.sleep(SLEEP_TIMEOUT)
            submitPressed += 1
            if submitPressed >= maxPress:
                time.sleep(k * SLEEP_TIMEOUT)
                submitPressed = 0
        except Exception:
            print("something is wrong with submit button")
            try_to_push(cart, submit)


def get_cart_link(driver):
    links = driver.find_elements_by_tag_name("a")
    cart = ""
    for lin in links:
        if lin.get_attribute("aria-label") == "Корзина":
            cart = lin
            break
    return cart


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

    submit = container.find_element_by_tag_name("div").find_element_by_tag_name("button")
    time.sleep(SLEEP_TIMEOUT)
    try_to_push(cart, submit)
    return True
