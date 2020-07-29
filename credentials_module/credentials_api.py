import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *

SLEEP_TIMEOUT = 1

# TODO: fill correct values
surname = "inputSurname"
name = "inputName"
patr = "inputPatr"
pcode = "420132"
shippingRegion = "Татарстан"
city = "Казань"
street_house_number = "kkjfajkfa,19"
flat_floor = "19,2,3"
pnumber = "88005553535"
email = "something@mail.ru"
cardnumber = "4263982640269299"
expiry_month = "04"
expiry_year = "23"
cvv = "738"


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
    buttons = driver.find_element_by_id("react-root").find_elements_by_tag_name("button")
    next_page_button = ""
    print("try to push button to make visible order button")
    for button in buttons:
        if button.get_attribute("data-automation") == "go-to-checkout-button":
            try:
                button.click()
            except Exception as e:
                print(str(e))
            print("button shows order button pressed")
            break
    while next_page_button == "":
        for button in buttons:
            if button.text == "Оформить заказ без регистрации":
                next_page_button = button
                break
    url = driver.current_url
    while driver.current_url == url:
        time.sleep(SLEEP_TIMEOUT)
        click(next_page_button)


def agree(checkbox):
    try:
        checkbox.click()
    except Exception as e:
        print(e)
        time.sleep(0.1)
        agree(checkbox)


def get_checkout_form(driver):
    try:
        return driver.find_element_by_name("checkout_form")
    except:
        time.sleep(0.1)
        get_checkout_form(driver)


def get_card_fields_iframe(driver):
    try:
        iframe = ""
        iframes = driver.find_elements_by_tag_name("iframe")
        for ifr in iframes:
            if ifr.get_attribute("class") == "paymentFrameApexx":
                iframe = ifr
                break
        driver.switch_to.frame(iframe)
    except Exception as e:
        print(str(e))
        time.sleep(0.3)
        get_card_fields_iframe(driver)


def fill_card_fields(driver):
    try:
        card_number_field = driver.find_element_by_id("card_number")
        card_number_field.send_keys(cardnumber)
        expiry_month_field = driver.find_element_by_id("expiry_month")
        expiry_month_field.send_keys(expiry_month)

        expiry_year_field = driver.find_element_by_id("expiry_year")
        expiry_year_field.send_keys(expiry_year)

        cvv_field = driver.find_element_by_id("cvv")
        cvv_field.send_keys(cvv)
        if card_number_field.get_attribute("value") != "" and expiry_month_field.get_attribute("value") != "" and \
                expiry_year_field.get_attribute("value") != "" and cvv_field.get_attribute("value") != "":
            driver.find_element_by_id("hostedPaymentsubmitBtn").click()
    except Exception as e:
        print(str(e))
        time.sleep(0.1)
        fill_card_fields(driver)


def fill_credentials(driver):
    print(driver.current_url)
    while not driver.current_url.startswith("https://secure-global.nike.com"):
        print(driver.current_url)
        time.sleep(0.1)
    firstForm = get_checkout_form(driver)
    firstForm.find_element_by_id("Shipping_LastName").send_keys(surname)
    firstForm.find_element_by_id("Shipping_FirstName").send_keys(name)
    firstForm.find_element_by_id("Shipping_MiddleName").send_keys(patr)
    firstForm.find_element_by_id("Shipping_PostCode").send_keys(pcode)
    Select(firstForm.find_element_by_id("Shipping_Region")) \
        .select_by_visible_text(shippingRegion)
    firstForm.find_element_by_id("Shipping_PostCode").send_keys(pcode)
    firstForm.find_element_by_id("Shipping_City").send_keys(city)
    firstForm.find_element_by_id("Shipping_Address1").send_keys(street_house_number)
    firstForm.find_element_by_id("Shipping_Address2").send_keys(flat_floor)
    firstForm.find_element_by_id("Shipping_phonenumber").send_keys(pnumber)
    firstForm.find_element_by_id("shipping_Email").send_keys(email)
    agreement_section = driver.find_element_by_id("gdprSection")

    agreement_checkbox = agreement_section.find_element_by_tag_name("span")
    agree(agreement_checkbox)

    driver.find_element_by_id("shippingSubmit").click()
    driver.find_element_by_id("billingSubmit").click()

    get_card_fields_iframe(driver)
    fill_card_fields(driver)
