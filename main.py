import os
import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json
from difflib import get_close_matches


driverPath = os.path.abspath(os.path.dirname(__file__)) + '/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(driverPath)
driver.get('https://nemexia.2axion.com/')

username = 'ur username'
password = 'ur password'

driver.find_element_by_name('username').send_keys(username)
driver.find_element_by_id('password').send_keys(password)


try:
    element = WebDriverWait(driver,3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="btn-login"]'))
    )
    element.click()
except:
    raise 'too long waiting time'


