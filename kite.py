#This is just a demo app to login into zerodha.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#read credentials from file
#its always safe to store credential in different file. 
#Saving credential in the script is not a good practise.
# f = open("cred.txt", "r")
# lines = f.readlines()
# #pass parameter based on your requirement
# usernameStr = lines[0] #username
# passwordStr = lines[1] #password
# pinStr = lines[2]      #pin
# f.close()
usernameStr = "NA5676" #username
passwordStr = "Vis@1829VS" #password
pinStr = "192996"      #pin

browser = webdriver.Firefox()
browser.get(('https://kite.zerodha.com/'))
signInButton= browser.find_element_by_css_selector('button.button-orange.wide')

# fill in username and hit the next button
username = browser.find_element_by_id('userid')
username.send_keys(usernameStr)

#click next input field
nextButton = browser.find_element_by_id('password')
nextButton.click()

# wait for transition then continue to fill items
password = WebDriverWait(browser, 2).until(EC.presence_of_element_located((By.ID, "password")))
password.send_keys(passwordStr)

#click button to continue
signInButton.click()

# wait for transition then continue to fill items

pin = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.ID, "pin")))
pin.send_keys(pinStr)

#click button to continue
signInButton.click()
