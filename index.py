from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotVisibleException,ElementNotSelectableException

from itertools import count 

driver = webdriver.Chrome('./driver/chromedriver') 
driver.get('https://web.whatsapp.com/')

wait = WebDriverWait(driver, 10, 
                     poll_frequency=1, 
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])

start = input('Enter despues de ingresar el codigo QR')

message = "test message"
contacts = ['"info1"','"info2"','"info3"']

message_path = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'

c = count(0)
while True:

    for contact in contacts: 

        # Contact
        contact_path = '//span[contains(@title,' + contact + ')]'   
        contact_box = driver.find_element_by_xpath(contact_path)
        contact_box.click()

        # Message
        message_box = driver.find_element_by_xpath(message_path) 
        # message_box = wait.until(EC.element_to_be_clickable((By.XPATH, message_path)))
        for i in range(50):
            message_box.send_keys(message + Keys.ENTER)

    print(next(c))