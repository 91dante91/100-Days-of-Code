import requests
from  bs4 import BeautifulSoup
from selenium import webdriver
import time


GOOGLE_FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLScNqUq1ssV_u__LjqMOu4wampMLe7vae3VzgmeLakFsVleXLQ/viewform?usp=sf_link"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
url_zillow = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64481581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A925766%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D"
headers = {
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url=url_zillow, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
all_link_elements = soup.select(".list-card-top a")
all_links = []
for link in all_link_elements:
    href = link["href"]
    if "https:" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)
print(all_links)
all_prices_elements = soup.select(".list-card-heading")
all_prices = []
for element in all_prices_elements:
    try:
        price = element.select(".list-card-price")[0].contents[0]
    except IndexError:
        print('Multiple listings for the card')
        price = element.select(".list-card-details li")[0].contents[0]
    finally:
        all_prices.append(price)


print(all_prices)
all_addr_elements = soup.select(".list-card-addr")
all_addrs = [addr.get_text().split("|")[-1] for addr in all_addr_elements]
print(all_addrs)
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

for n in range(len(all_links)):
    driver.get(GOOGLE_FORM_LINK)

    time.sleep(2)
    address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')

    address.send_keys(all_addrs[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()