from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#read credentials from file
f = open("cred.txt", "r")
lines = f.readlines()
usernameStr = lines[0]
passwordStr = lines[1]
pinStr = lines[2]
f.close()


browser = webdriver.Firefox()
browser.get(('https://kite.zerodha.com/'))
signInButton= browser.find_element_by_css_selector('button.button-orange.wide')
# fill in username and hit the next button
username = browser.find_element_by_id('userid')
username.send_keys(usernameStr)

nextButton = browser.find_element_by_id('password')
# nextButton = browser.find_element_by_xpath("//form[@id='login-form']/input[2]")
nextButton.click()

# wait for transition then continue to fill items

password = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, "password")))
password.send_keys(passwordStr)

signInButton.click()

# wait for transition then continue to fill items

pin = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "pin")))
pin.send_keys(pinStr)

signInButton.click()
