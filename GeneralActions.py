import os
import random
import select
import sys
import time
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GeneralActions():
    def __init__(self, driver):
        self.driver = driver

    def resetActivityProtection(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="serverTimeDisplay"]'))
        )
        element.click()

        # click on verification and w8 for human selecting pictures
        WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//*[@id="pageBody"]/div[5]/div/form/center/div/div/div/iframe')))
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]/div[1]'))
        )
        element.click()
        self.driver.switch_to.default_content()
        time.sleep(random.uniform(17, 18))
        element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pageBody"]/div[5]/div/form/center/input'))
        )
        element.click()

        time.sleep(random.uniform(2, 3))
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pageBody"]/div[5]/div/form/center/input'))
        )
        element.click()
        time.sleep(random.uniform(2, 3))

