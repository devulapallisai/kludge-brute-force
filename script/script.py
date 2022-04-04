from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tomlkit import value
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def launchBrowser():
    username = "hello@gmail.com"
    # password = "correct"
    for password in passwords:
        options = Options()

    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=Service(
            ChromeDriverManager().install()))
        options.add_argument("start-maximized")
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver.get("http://localhost:5000")
        time.sleep(2)
        username_in_website = driver.find_element(
            By.XPATH, value='//*[@id="form2Example1"]')
        username_in_website.send_keys(username)
        password_in_website = driver.find_element(
            By.XPATH, value='//*[@id="form2Example2"]')
        password_in_website.send_keys(password)

        submit = driver.find_element(
            By.XPATH, value="/html/body/form/div/div[2]/button")

        submit.click()
    return driver


with open("passwords.txt", "r") as passwords:
    driver = launchBrowser()
