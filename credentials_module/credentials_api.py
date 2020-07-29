import time

from selenium.common.exceptions import StaleElementReferenceException


def click(b):
    time.sleep(0.1)
    try:
        # TODO: properly works
        b.click()
        print(b.text)
        return
    except StaleElementReferenceException:
        return
    except Exception as e:
        print(str(e))
        click(b)
        return


def go_to_credentials_page(driver):
    buttons = driver.find_elements_by_tag_name("button")
    nextPageButton = ""
    print("try to push button to make visible order button")
    for button in buttons:
        if button.get_attribute("data-automation") == "go-to-checkout-button":
            button.click()
            print("button shows order button pressed")
            break
        if button.get_attribute("data-automation") == "guest-checkout-button":
            nextPageButton = button

    if nextPageButton == "":
        for button in buttons:
            if button.get_attribute("data-automation") == "guest-checkout-button":
                nextPageButton = button
                break
    url = driver.current_url
    while driver.current_url == url:
        click(nextPageButton)


def fill_credentials(driver):
    print(driver.current_url)
