#! python3
# main-login.py - Simple script that download all photos from an Instagram profile (LogIn manually).

import logging, time, requests, os, re, pprint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s -  %(levelname)s -   %(message)s')
logging.disable(logging.DEBUG)

def get_profile_info(profile):
    profileInfo = profile.find_element(By.CLASS_NAME, 'xdj266r') 
    infoByLines = str(profileInfo.text).split('\n')
    # logging.info(infoByLines)
    info = {}
    info['username'] = infoByLines[0]
    info['posts'] = infoByLines[3].split(' ')[0]
    info['followers'] = infoByLines[4].split(' ')[0]
    info['following'] = infoByLines[5].split(' ')[0]
    info['name'] = infoByLines[6]
    # info['bio'] = infoByLines[7]
    return info

def get_users(browser):

    scrollable_div  = browser.find_element(By.CSS_SELECTOR, ".x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.x1sxyh0.xurb0ha.x1uhb9sk.x6ikm8r.x1rife3k.x1iyjqo2.x2lwn1j.xeuugli.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1.x1l90r2v")
    usersList = []
    
    Flag = True
    while Flag:
        # Look if we are in the final of the div
        at_bottom = browser.execute_script(
            "return arguments[0].scrollTop + arguments[0].clientHeight >= arguments[0].scrollHeight;", 
            scrollable_div)
        if at_bottom:
            logging.info("Ya estás en el final del scroll.")
            Flag = False  
        else:
            usersElem = browser.find_elements(By.CLASS_NAME, "x1rg5ohu")
            for i in range(len(usersElem)):
                if usersElem[i].text not in usersList:
                    usersList.append(str(usersElem[i].text))
                    logging.info(str(usersElem[i].text))

            time.sleep(1)
            browser.execute_script("arguments[0].scrollTop += 800;", scrollable_div)
            time.sleep(2)
    return usersList
    

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
    logging.info(pprint.pformat(profileInfo))
    time.sleep(2)

    # TODO: Click into the following part
    followingElem = browser.find_element(By.PARTIAL_LINK_TEXT, 'following')
    followingElem.click()
    time.sleep(2)
    print("Starting scrap...")
    time.sleep(4)
    #   TODO: Download the users in a lists and do scroll
    followingList = get_users(browser)
    
    # TODO: Click into the following part
    #   TODO: Download the users in a lists and do scroll

    # TODO: Write the lists in a TXT / PDF

except NoSuchElementException:
    logging.error("Was not able to find an element with that class name.")

finalList = followingList[1:]

print(f"Following: {len(finalList)} users")
pprint.pprint(finalList)


print("\n\nThanks for scrapping with us, come again soon!!<3<3 \n\n")
input("ENTER TO CLOSE...")
browser.quit()