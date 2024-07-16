from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time


browser = Firefox()
link = "https://www.google.com.br"
browser.get(link)

input_area = browser.find_element(By.NAME,"q")
input_area.send_keys("Instituto Joga Junto"),
input_area.send_keys(Keys.ENTER)

result = browser.find_element(By.TAG_NAME,'h3')


for i in result:
    if "instituto Joga Junto" in i.text:
        result.click()
        


