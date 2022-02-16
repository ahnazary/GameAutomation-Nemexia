import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GameActions:
    def __init__(self, driver):
        self.driver = driver

    def initialLogin(self):
        # login
        username = '' # 'ur username'
        password = '' # 'ur password'
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_id('password').send_keys(password)

        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div/div[1]/div/div/button'))
        )
        element.click()
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div/div[1]/div/div/div/ul/li[1]/a'))
        )
        element.click()
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="btn-login"]'))
        )
        element.click()
        time.sleep(8)

        # closing popups
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="dialogBox"]/div/div[3]/input'))
        )
        element.click()
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="treasureHuntingPopup_closeButton"]'))
        )
        element.click()
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="dialogBox"]/a'))
        )
        element.click()

        # mute sound
        element = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="audioManagerMute"]'))
        )
        element.click()

    def goToFleetPage(self):
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="globalMenu"]/ul/li[2]'))
        )
        element.click()
        time.sleep(1)
        # changing planet
        element = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="planetSwitch"]/div[2]'))
        )
        element.click()
        time.sleep(1)
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="planetsListHolder"]/li[4]/a'))
        )
        element.click()

    def infinitePirateflight(self, coordinate, shipsNumber, attackTimes, activeFlightsNumber):
        i = 0
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="FleetsCount"]'))
        )
        while True:
            time.sleep(5)
            print(element.text)
            if element.text == str(activeFlightsNumber):
                while i < attackTimes:
                    self.sendPirateAttacks(coordinate, shipsNumber)
                    i += 1

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

        time.sleep(6)
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

        # self.driver.find_element_by_xpath('//*[@id="target_c1"]').clear()
        # self.driver.find_element_by_xpath('//*[@id="target_c1"]').send_keys(coordinate[0])
        # self.driver.find_element_by_xpath('//*[@id="target_c2"]').clear()
        # self.driver.find_element_by_xpath('//*[@id="target_c2"]').send_keys(coordinate[1])
        # self.driver.find_element_by_xpath('//*[@id="target_c3"]').clear()
        # self.driver.find_element_by_xpath('//*[@id="target_c3"]').send_keys(coordinate[2])
        element = WebDriverWait(self.driver, 25).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="SendFleetButton"]'))
        )
        element.click()
        time.sleep(4)
