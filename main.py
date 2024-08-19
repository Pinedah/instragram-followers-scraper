#! python3
# main-login.py - Simple script that download all photos from an Instagram profile (LogIn manually).

import logging, time, requests, os, re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.DEBUG)

def get_profile_info(profile):
    profileInfo = profile.find_element(By.CLASS_NAME, 'xdj266r') 
    infoByLines = str(profileInfo.text).split('\n')
    logging.info(infoByLines)
    info = {}
    info['username'] = infoByLines[0]
    info['posts'] = infoByLines[3].split(' ')[0]
    info['followers'] = infoByLines[4].split(' ')[0]
    info['following'] = infoByLines[5].split(' ')[0]
    info['name'] = infoByLines[6]
    # info['bio'] = infoByLines[7]
    return info

# -------------------- BEGIN CODE -----------------------------------------------
# TODO: Add Main and UI !!

print("\n--- Please checkout the README file before using the script :). ---\n")
print("Login into your account and then go to the profile you want to scrapp.")
print("When you are ready, press ENTER in the console to begin the downloads.\n\n")

# Initialize browser object
browser = webdriver.Chrome()
browser.get('https://www.instagram.com/')
time.sleep(2)

input() # Press ENTER to continue

try:
    htmlElem = browser.find_element(By.TAG_NAME, 'html')
    time.sleep(4)
    profileInfo = get_profile_info(browser)
    logging.info(profileInfo)
    time.sleep(2)
except NoSuchElementException:
    print("Was not able to find an element with that class name.")


print("Thanks for scrapping with us, come again soon!!<3<3 \n\n")

browser.quit()