from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time

def add_friend(driver,uname):
    driver.get( 'https://codeforces.com/profile/' + uname)
    time.sleep(1)
    try:
        star = driver.find_element_by_class_name('addFriend')
        star.click()
        print(uname+" Added as friend")
    except:
        print(uname + " Already a friend or doesn't exist")


driver = webdriver.Chrome('./chromedriver')

driver.get('https://codeforces.com/enter')


username = driver.find_element_by_xpath('//*[@id="handleOrEmail"]')
username.send_keys('Your username')

passw = driver.find_element_by_xpath('//*[@id="password"]')
passw.send_keys('Your_password')
time.sleep(1)


butt = driver.find_element_by_xpath('/html/body/div[5]/div[4]/div/div/div/form/table/tbody/tr[4]/td/div[1]/input')
butt.click()
time.sleep(1)

file = open('file.txt','r')

for user in file:
    add_friend(driver,user)

driver.quit()