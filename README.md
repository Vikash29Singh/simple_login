# Automatic Kite Login 
Prerequisite
- Install Python
- Install Selenium

I am assuming you have already installed the python.
 
 ## Install Selenium
 ```
  pip install -U Selenium 
 ```
 This command will successfully install the latest Selenium package

 ## Import libraries
 - Step 1: import the web driver
 - Step 2: import WebDriverWait.
 Web driver wait take two parameter. 
    - browser
    - wait time.
- Step 3: EC is expected_conditions. An operation will be performed only after the condition is fulfilled and presence_of_element_located.
 ```
from selenium import webdriver  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
```
## Select browser
In my case, I have used firefox.
```
browser = webdriver.Firefox()
```
### For more details [click me.](https://www.selenium.dev/documentation/en/webdriver/driver_requirements/)


## Redirect
This will navigate to the given URL
```
browser.get(('https://www.google.com/'))
```

## Locating element
For more detail [click me.](https://selenium-python.readthedocs.io/locating-elements.html)

# Make python file executable

The first step is to install PyInstaller from PyPI. 
~~~
pip install pyinstaller
~~~
Once installed successfully go to the directory you have installed the .py file
~~~
pyinstaller --onefile Yourfilename.py
~~~
Your executable file is successfully created.

### This command will create additional files and folders. Once creation is completed, navigate to 'dist' folder and "Voila!" you will see executable file. Run the file.
<br>

### <span style="color:red">Note:- </span>To execute my code, first make changes in the "cred.txt" file and save the file in dist folder, where executable is generated. <span style="color:red">Or</span> instead of creating the separate credential file, simply add the credential in your main python file and then run the pyinstaller instruction as above. Now, all you need to do is run the executable file once created successfully.
<br>

To know more visit [pypi](https://pypi.org/project/pyinstaller/) or [realpython](https://realpython.com/pyinstaller-python/#using-pyinstaller)





