from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

#os.environ["SELENIUM_SERVER_JAR"] = "selenium-server-standalone-3.0.1.jar"
# note: I've put this jar file in the same folder as this python file

browser = webdriver.Safari()

# makes the browser wait if it can't find an element
browser.implicitly_wait(10)

browser.get("http://google.com/")

search_input = browser.find_element_by_css_selector("#gbqfq")
search_input.send_keys("python SELENIUM_SERVER_JAR turn logging off")
search_input.send_keys(Keys.RETURN)

raw_input("Press Enter to close...")

browser.quit()
