import os

from selenium import webdriver
from GameActions import GameActions


driverPath = os.path.abspath(os.path.dirname(__file__)) + '/chromedriver_linux64/chromedriver'
driver = webdriver.Chrome(driverPath)
driver.get('https://nemexia.2axion.com/')

actions = GameActions(driver)
actions.initialLogin()
# actions.getInactiveCoordinates()
actions.autoRefresh()
