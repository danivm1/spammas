# coding=<unicode>
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Opera()

driver.set_page_load_timeout(30)
driver.get("https://discord.com/login")

email = ''
password = ''

driver.find_element_by_name('email').send_keys(email)

driver.find_element_by_name('password').send_keys(password, Keys.ENTER)

time.sleep(10)

driver.get("https://discord.com/channels/761990759376224336/761990759376224339")

# actions = ActionChains(driver)

while True:
    # actions.send_keys('É o spammas?', Keys.ENTER)
    driver.find_element_by_tag_name('body').send_keys(':rage: Gank do spammas :rage:', Keys.ENTER)