from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def push_button(XPath):
    try:
        smth =  driver.find_element_by_xpath(XPath)
        if smth != None:
            smth.click()
    except:
        return True
    return False

def send_inf(XPath, text):
    try:
        smth =  driver.find_element_by_xpath(XPath)
        if smth != None:
            smth.send_keys(text)
    except:
        return True
    return False


driver = webdriver.Chrome(ChromeDriverManager().install())

start_time=time.time()

driver.get("https://www.nike.com/ru/launch/t/air-force-1-craft-vast-grey")

middle_time=time.time()

while push_button('//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/ul/li[9]/button'):
    pass
while push_button('//*[@id="root"]/div/div/div[2]/div/div/div/div/div[3]/button[2]'):
    push_button('//*[@id="root"]/div/div/div[1]/div/div[3]/div[2]/div/section[1]/div[2]/aside/div/div[2]/div/div[2]/div/button')
    time.sleep(0.1)
while send_inf('//*[@id="Shipping_LastName"]', "Ты"):
    pass
send_inf('//*[@id="Shipping_FirstName"]', "Кто")
send_inf('//*[@id="Shipping_MiddleName"]', "Пожизни?")
send_inf('//*[@id="Shipping_PostCode"]', "420140")
send_inf('//*[@id="Shipping_City"]', "Казань")
send_inf('//*[@id="Shipping_Address1"]', "кек 24")
send_inf('//*[@id="Shipping_phonenumber"]', "89999999999")
send_inf('//*[@id="shipping_Email"]', "lohlohloh@mail.ru")
driver.find_element_by_xpath('//*[@id="gdprSection"]/div[1]/label[1]/span').click()
driver.find_element_by_xpath('//*[@id="shippingSubmit"]').click()
driver.find_element_by_xpath('//*[@id="billingSubmit"]').click()
while send_inf('//*[@id="card_number"]', '8888888888888888'):
    try:
        driver.switch_to.frame(driver.find_element_by_xpath('//*[@id="slidePayment"]/div[2]/div/div[2]/div/div[2]/div/iframe'))
    except:
        pass
send_inf('//*[@id="expiry_month"]', '12')
send_inf('//*[@id="expiry_year"]', "20")
send_inf('//*[@id="cvv"]', "123")
driver.quit()
print(time.time()-middle_time)
print(time.time()-start_time)
time.sleep(10)