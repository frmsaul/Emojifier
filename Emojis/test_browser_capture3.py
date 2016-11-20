from base64 import b64decode
from wand.image import Image
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import math
import os

HTML_FOLDER_URL = 'file:///Users/saulfuhrmann/Computers/SalamProject/Emojis/BrowserPreProcessing/HTML_FILES'


def save_element_screenshot(element,
                           file_name):
    driver = element._parent
    ActionChains(driver).move_to_element(element).perform()  # focus
    src_base64 = driver.get_screenshot_as_base64()
    scr_png = b64decode(src_base64)
    scr_img = Image(blob=scr_png)

    x = element.location["x"]
    y = element.location["y"]
    w = element.size["width"]
    h = element.size["height"]
    scr_img.crop(
        left=int(math.floor(x)),
        top=int(math.floor(y)),
        width=int(math.ceil(w)) + 1,
        height=int(math.ceil(h)) + 1,
    )
    with open(file_name, "w") as f:
        f.write(scr_img.make_blob());
    return 

if __name__ == "__main__":
    browser = webdriver.Chrome("./BrowserPreProcessing/chromedriver")
    #browser = webdriver.Firefox()

    browser.get(HTML_FOLDER_URL + "/Emojis4.html")
    #browser.save_screenshot('screenie.png')
    table = browser.find_element_by_tag_name("table")

    emojis =  table.find_elements_by_class_name("emoji")
    save_element_screenshot(emojis[2],
                           "test_shot.png")
    
    browser.quit()
    os.system("rm geckodriver.log");
