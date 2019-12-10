from selenium import webdriver
import time

cont = 0
user = 'lopescwb'
passs = 'Magnata643@'
url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
driver = webdriver.Chrome("/Users/victo/Desktop/shell/chromedriver")
driver.get(url)
time.sleep(2)
driver.find_element_by_name('username').send_keys(user)
time.sleep(3)
driver.find_element_by_name('password').send_keys(passs)
time.sleep(3)
driver.find_element_by_class_name('sqdOP.L3NKy.y3zKF').click()
time.sleep(6)
driver.get('https://www.instagram.com/p/B5vtCWXB7bw/?igshid=v1c89359kpzm')
time.sleep(6)
driver.find_element_by_class_name('Ypffh').click()
time.sleep(6)

arq = open('FOLLOWS.txt', 'r')
for linha in arq :
    driver.find_element_by_class_name('Ypffh').send_keys(arq.readline())
    cont += 1
    print(cont)
    # driver.find_element_by_class_name('Ypffh').send_keys(arq.readline().rstrip() + " ",arq.readline().rstrip() + " ", arq.readline())
    time.sleep(300)
    # print(arq.readline().rstrip(), arq.readline().rstrip(), arq.readline())
    # driver.find_element_by_class_name('sqdOP.yWX7d.y3zKF').click()
    # time.sleep(10)
