from selenium.common.exceptions import *

SLEEP_TIMEOUT = 0

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
    button = driver.find_element_by_xpath(
        "/html[@class='no-scroll']/body/div[@id='root']/div[@class='u-full-width u-full-height']/div[@class='root-controller remove-outline no-scroll']/div[@class='js-modal modal show']/div[@class='modal-scroll-container u-full-height']/div[@class='d-md-t u-full-height u-full-width p0-sm']/div[@class='d-md-tc u-full-width u-full-height va-sm-t']/div[@class='cart-item-modal-content-container ncss-container p6-sm bg-white']/div[@class='ncss-row cart-button-row']/button[@class='ncss-btn-black ncss-brand fs16-sm pt3-sm pr5-sm pb3-sm pl5-sm mt4-sm mr4-sm u-uppercase cart-link']")
    button.click()


def agree(checkbox):
    try:
        checkbox.click()
    except Exception as e:
        print(e)
        agree(checkbox)


def get_checkout_form(driver):
    try:
        res = driver.find_element_by_name("checkout_form")
        if res is not None:
            return res
    except:
        return get_checkout_form(driver)


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
        get_card_fields_iframe(driver)


def fill_card_fields(driver):
    try:
        card_number_field = driver.find_element_by_xpath('//*[@id="card_number"]')
        card_number_field.send_keys(cardnumber)
        expiry_month_field = driver.find_element_by_xpath('//*[@id="expiry_month"]')
        expiry_month_field.send_keys(expiry_month)

        expiry_year_field = driver.find_element_by_xpath('//*[@id="expiry_year"]')
        expiry_year_field.send_keys(expiry_year)

        cvv_field = driver.find_element_by_xpath('//*[@id="cvv"]')
        cvv_field.send_keys(cvv)
        if card_number_field.get_attribute("value") != "" and expiry_month_field.get_attribute("value") != "" and \
                expiry_year_field.get_attribute("value") != "" and cvv_field.get_attribute("value") != "":
            # TODO:CHANGE THIS SHIT
            driver.quit()
            return
            driver.find_element_by_xpath("//*[@id='hostedPaymentsubmitBtn']").click()
    except Exception as e:
        print(str(e))
        fill_card_fields(driver)


def fill_credentials(driver):
    firstForm = get_checkout_form(driver)
    firstForm.find_element_by_xpath('.//*[@id="Shipping_LastName"]').send_keys(surname)
    firstForm.find_element_by_xpath('.//*[@id="Shipping_FirstName"]').send_keys(name)
    firstForm.find_element_by_xpath('.//*[@id="Shipping_MiddleName"]').send_keys(patr)
    firstForm.find_element_by_xpath('.//*[@id="Shipping_PostCode"]').send_keys(pcode)
    # Select(firstForm.find_element_by_id("Shipping_Region")) \
    #    .select_by_visible_text(shippingRegion)
    firstForm.find_element_by_xpath('.//*[@id="Shipping_PostCode"]').send_keys(pcode)
    firstForm.find_element_by_xpath('.//*[@id="Shipping_City"]').send_keys(city)
    firstForm.find_element_by_xpath('.//*[@id="Shipping_Address1"]').send_keys(street_house_number)
    firstForm.find_element_by_xpath('.//*[@id="Shipping_Address2"]').send_keys(flat_floor)
    firstForm.find_element_by_xpath('.//*[@id="Shipping_phonenumber"]').send_keys(pnumber)
    firstForm.find_element_by_xpath('.//*[@id="shipping_Email"]').send_keys(email)
    agreement_section = driver.find_element_by_xpath('.//*[@id="gdprSection"]')

    agreement_checkbox = agreement_section.find_element_by_tag_name("span")
    agree(agreement_checkbox)

    driver.find_element_by_xpath('.//*[@id="shippingSubmit"]').click()
    driver.find_element_by_xpath('.//*[@id="billingSubmit"]').click()

    get_card_fields_iframe(driver)
    fill_card_fields(driver)
