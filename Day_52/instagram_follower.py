from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time
import re

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "Similar Account"
USERNAME = "Your user name"
PASSWORD = "Your password"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        name = self.driver.find_element_by_name("username")
        password = self.driver.find_element_by_name("password")
        name.send_keys(USERNAME)
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/")
        followers = self.driver.find_element_by_css_selector(".Y8-fY a")
        followers_count = int(re.sub(r'(\d)\s+(\d)', r'\1\2', self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').get_attribute('title')))
        followers.click()
        time.sleep(3)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(followers_count // 2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

    def follow(self):
        all_button = self.driver.find_elements_by_css_selector("li button")
        for button in all_button:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_btn = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]')
                cancel_btn.click()





insta = InstaFollower()
insta.login()
time.sleep(3)
insta.find_followers()
insta.follow()
