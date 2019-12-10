from selenium import webdriver
import time

from selenium import webdriver
import time

# CONNECT PAGE

cont = 0
user = 'NegoJao'
passs = '7a5ca2d17aa7'
url = 'https://www.thecrims.com/'
driver = webdriver.Chrome("/Users/victo/Desktop/shell/chromedriver")
driver.get(url)

time.sleep(2)
# LOGIN PAGE
    # INPUTS
time.sleep(5)
driver.find_element_by_link_text('Username').send_keys(user)
time.sleep(5)
driver.find_element_by_name('password').send_keys(passs)
time.sleep(5)

# BUTTON
driver.find_element_by_css_selector('btn.btn-large.btn-inverse').click()
