try:
    import os
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import time

    print("\nWhat movie would you like to download? Be specific for better results.")
    movie_name = input()

    prefs = {"protocol_handler.excluded_schemes":{"magnet":False}}    
    rel_path = os.path.dirname(__file__)
    path = rel_path+"\chromedriver.exe"

    print("\nOpening browser..")
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(executable_path=path, options = chrome_options)
    driver.get("https://thepiratebay.org")
    print("\nWaiting for the pirate bay.. \n")

    element = driver.switch_to.active_element
    element.send_keys(movie_name)
    element.submit()

    seeders = driver.find_element_by_css_selector("#torrents > li.list-header > span.list-item.list-header.item-leech > label")
    time.sleep(0.5)
    seeders.click()

    download = driver.find_element_by_css_selector("#st > span.item-icons > a")
    download.click()

    time.sleep(1)
    print("Sucessful lmao\n")
    driver.quit()
    exit(15)
except ImportError:
    print("\nThe module selenium is required; \nrun: pip install selenium\n")

