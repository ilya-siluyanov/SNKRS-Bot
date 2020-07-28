import time


def is_cart_empty(cart):
    try:
        cart.find_element_by_tag_name("span")
        return False
    except Exception as e:
        print(str(e))
        return True


def try_to_push(cart, submit):
    while is_cart_empty(cart):
        time.sleep(0.1)
        try:
            submit.click()
        except Exception:
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
    driver.get(link)
    cart = get_cart_link(driver)
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
            found = True
            break
    if not found:
        return False

    submit = container.find_element_by_tag_name("div").find_element_by_tag_name("button")
    try_to_push(cart, submit)
    return True
