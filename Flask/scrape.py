from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "C:\\Users\\Chairman APGB\\Desktop\\WEB_DEV\\chromedriver.exe"
chrome_service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.youtube.com/results?search_query=Web+Development")
XPATH_HREF = '//*[@id="content"]/a'

# continue_link = driver.find_element(By.TAG_NAME, 'a')
elem = driver.find_elements(By.XPATH, XPATH_HREF)
#x = str(continue_link)
#print(continue_link)
print(elem)

# string = "Web Development"
# query = f"https://www.youtube.com/results?search_query={string.replace(' ','+')}"
# LINK_SELECTOR = ".ytd-playlist-renderer"
# response = requests.get(url=query)
# website = response.text
# print(website)
# soup = BeautifulSoup(website, "html.parser")
# # "yt-simple-endpoint style-scope ytd-playlist-renderer"
# # "yt-simple-endpoint style-scope ytd-playlist-renderer"
#
# useful_links = list()
# for anchor_tag in soup.select(LINK_SELECTOR):
#     useful_links.append(anchor_tag["href"])
#
# print(useful_links)
