from selenium import webdriver
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")
items = driver.find_elements_by_css_selector("#store div")
items_ids = [item.get_attribute("id") for item in items]


timeout = time.time() + 5
five_minute = time.time() + 60 * 5

while True:
    cookie.click()
    if time.time() > timeout:
        if int(driver.find_element_by_id("money").text.replace(",", "")) > int(driver.find_element_by_css_selector("#buyTime\ machine b").text.split("-")[1].strip().replace(",", "")):
            driver.find_element_by_id("buyTime\ machine").click()
        elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(driver.find_element_by_css_selector("#buyPortal b").text.split("-")[1].strip().replace(",", "")):
            driver.find_element_by_id("buyPortal").click()
        elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(driver.find_element_by_css_selector("#buyAlchemy\ lab b").text.split("-")[1].strip().replace(",", "")):
            driver.find_element_by_id("buyAlchemy\ lab").click()
        elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(driver.find_element_by_css_selector("#buyShipment b").text.split("-")[1].strip().replace(",", "")):
            driver.find_element_by_id("buyShipment").click()
        elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(driver.find_element_by_css_selector("#buyMine b").text.split("-")[1].strip().replace(",", "")):
            driver.find_element_by_id("buyMine").click()
        elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(driver.find_element_by_css_selector("#buyFactory b").text.split("-")[1].strip().replace(",", "")):
            driver.find_element_by_id("buyFactory").click()
        elif int(driver.find_element_by_id("money").text.replace(",", "")) > int(driver.find_element_by_css_selector("#buyGrandma b").text.split("-")[1].strip().replace(",", "")):
            driver.find_element_by_id("buyGrandma").click()
        else:
            driver.find_element_by_id("buyCursor").click()

        timeout = time.time() + 30

        if time.time() > five_minute:
            print(driver.find_element_by_id("cps").text)
            break
