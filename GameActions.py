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
from GeneralActions import GeneralActions


class GameActions(GeneralActions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def initialLogin(self):
        # login
        self.driver.maximize_window()
        username = ''  # 'ur username'
        password = ''  # 'ur password'
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)

        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div/div[1]/div/div/button'))
        )
        element.click()

        # server selction
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div/div[1]/div/div/div/ul/li[3]/a/span[1]'))
        )
        element.click()
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="btn-login"]'))
        )
        element.click()

        # waiting for human to select pictures

        # closing popups
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="dialogBox"]/a'))
        )
        element.click()

        # mute sound
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="audioManagerMute"]'))
        )
        element.click()

    def autoRefresh(self):
        numberOfRefreshes = 0
        while True:
            try:
                element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="newAttackMsg"]'))
                )
                print("attack incoming...")
                for i in range(0, 50):
                    duration = 0.5  # seconds
                    freq = 350  # Hz
                    os.system('play -nq -t alsa synth {} sine {}'.format(duration, freq))
                    time.sleep(2)
                    i, o, e = select.select([sys.stdin], [], [], 3)

                    if i:
                        print("alert stopped.")
                        break
                    else:
                        print("You said nothing! alert continues ...")
            except:
                print('no attack coming')
                pass

            xpath = '//*[@id="globalMenu"]/ul/li[{}]'.format(random.randint(1, 6))
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element.click()
            randSleepTime = random.uniform(250, 350)
            print(datetime.now(), ': long sleep for {} seconds'.format(randSleepTime))
            time.sleep(randSleepTime)
            self.resetActivityProtection()

    def getInactiveCoordinates(self):
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="globalMenu"]/ul/li[3]'))
        )
        element.click()
        time.sleep(random.uniform(1, 2))

        # click advanced search
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="galaxyAdditional"]/li[4]/a'))
        )
        element.click()
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="buildingInfo"]/div[2]/ul/li[2]'))
        )
        element.click()
        time.sleep(random.uniform(1, 2))

        self.driver.find_element_by_xpath('//*[@id="txt_c1_down"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txt_c1_down"]').send_keys(1)
        self.driver.find_element_by_xpath('//*[@id="txt_c2_down"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txt_c2_down"]').send_keys(1)
        self.driver.find_element_by_xpath('//*[@id="txt_c1_up"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txt_c1_up"]').send_keys(2)
        self.driver.find_element_by_xpath('//*[@id="txt_c2_up"]').clear()
        self.driver.find_element_by_xpath('//*[@id="txt_c2_up"]').send_keys(40)
        time.sleep(random.uniform(1, 2))
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pointsSearchForm"]/div[8]/input'))
        )
        element.click()
        time.sleep(random.uniform(1, 2))
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="pointsResults"]/table'))
        )
        rows = element.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            columns = row.find_elements(By.TAG_NAME, "td")
            for item in columns:
                pass

    def goToFleetPage(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="planetSwitch"]/div[2]'))
        )
        element.click()
        time.sleep(random.uniform(1, 2))
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="planetsListHolder"]/li[4]/a'))
        )
        element.click()

    def infinitePirateFlight(self, coordinate, shipsNumber, attackTimes, activeFlightsNumber):
        i = 0
        while True:
            time.sleep(random.uniform(3, 6))
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="globalMenu"]/ul/li[2]'))
            )
            element.click()
            time.sleep(random.uniform(7, 15))
            element = WebDriverWait(self.driver, 25).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="FleetsCount"]'))
            )
            print(datetime.now(), ": ", element.text)
            if element.text != str(15):
                if element.text == str(activeFlightsNumber) or element.text == "" or int(element.text) <= 14:
                    while i < attackTimes:
                        self.sendPirateAttacks(coordinate, shipsNumber)
                        i += 1
                    i = 0
                    print("long sleep ...")
                    time.sleep(random.uniform(120, 180))

            xpath = '//*[@id="globalMenu"]/ul/li[{}]'.format(random.randint(1, 6))
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element.click()
            time.sleep(random.uniform(15, 25))

    def sendPirateAttacks(self, coordinate, numOfShips):
        self.driver.find_element_by_xpath('//*[@id="ship_2_3"]').send_keys(numOfShips)

        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="selectMissionImg-7"]'))
        )
        element.click()
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.NAME, 'continue'))
        )
        element.click()

        time.sleep(random.uniform(6, 8))
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="target_c1"]'))
        )
        element.clear()
        element.send_keys(coordinate[0])

        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="target_c2"]'))
        )
        element.clear()
        element.send_keys(coordinate[1])

        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="target_c3"]'))
        )
        element.clear()
        element.send_keys(coordinate[2])

        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="SendFleetButton"]'))
        )
        element.click()
        time.sleep(random.uniform(5, 6))
