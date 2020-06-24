from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

print("What movie would you like to download?")
movie_name = input()

prefs = {"protocol_handler.excluded_schemes":{"magnet":False}}
path = r"chromedriver.exe"

print("Opening browser..")
chrome_options = Options()
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(path, options = chrome_options)
driver.get("https://thepiratebay.org")
print("\nWaiting for the pirate bay.. \n")

element = driver.switch_to.active_element
element.send_keys(movie_name)
element.submit()

seeders = driver.find_element_by_css_selector("#torrents > li.list-header > span.list-item.list-header.item-leech > label")
seeders.click()

download = driver.find_element_by_css_selector("#st > span.item-icons > a")
download.click()

time.sleep(1)
print("Sucessful lmao\n")
driver.quit()


