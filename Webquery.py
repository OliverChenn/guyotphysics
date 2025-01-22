from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# https://stackoverflow.com/questions/56155010/how-to-click-a-web-browser-button-using-python
# Used this for inspiration of pip install

driver_path = "path/to/chromedriver"

driver = webdriver.Chrome(executable_path=driver_path)

try:
    # Open a website
    driver.get("https://earthquake.usgs.gov/earthquakes/search/")
    time.sleep(2)

    search_box = driver.find_element(By.NAME, "Minimum")
    search_box.send_keys("0")
    search_box.send_keys(Keys.RETURN)

    search_box = driver.find_element(By.NAME, "Maximum")
    search_box.send_keys("10")
    search_box.send_keys(Keys.RETURN)

    search_box = driver.find_element(By.NAME, "Start (UTC)")
    search_box.send_keys("2024-03-31 00:00:00")
    search_box.send_keys(Keys.RETURN)

    search_box = driver.find_element(By.NAME, "End (UTC)")
    search_box.send_keys("2024-04-31 23:59:59")
    search_box.send_keys(Keys.RETURN)

    search_box = driver.find_element(By.NAME, "End (UTC)")
    search_box.send_keys("2024-04-31 23:59:59")
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)



finally:
    # Close the browser
    driver.quit()