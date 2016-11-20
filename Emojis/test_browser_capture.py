import os
from selenium import webdriver

HTML_FOLDER_URL = 'file:///Users/saulfuhrmann/Computers/SalamProject/Emojis/BrowserPreProcessing/HTML_FILES'

if __name__ == "__main__":
    #browser = webdriver.Chrome("./BrowserPreProcessing/chromedriver")
    browser = webdriver.Firefox()


    browser.get(HTML_FOLDER_URL + "/Emojis0.html")
    browser.save_screenshot('screenie.png')
    table = browser.find_element_by_tag_name("table")
    emojis =  table.find_elements_by_class_name("emoji")

    #    print dir(emojis[50])
    # table.screenshot("Test")
    # emojis[50].screenshot("Emoji50.png")
    # Clean up
    browser.quit()
    os.system("rm geckodriver.log");




