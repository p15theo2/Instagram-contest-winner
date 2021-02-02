from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import os
import commentslist
from datetime import datetime

class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get('https://instagram.com')
        time.sleep(1)
        # cookie 
        cookie_button = driver.find_element_by_xpath("//button[text()='Accept']")
        cookie_button.click()

        time.sleep(2)
        username_elem = driver.find_element_by_xpath('//input[@name="username"]')
        username_elem.clear()
        username_elem.send_keys(self.username)
        time.sleep(3)
        password_elem = driver.find_element_by_xpath('//input[@name="password"]')
        password_elem.clear()
        password_elem.send_keys(self.password)
        time.sleep(3)
        login_button = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
        login_button.click()

    def endOfProccess(self, text):
        self.driver.get(text)

    def addComment(self,link,tags):
        driver_c = self.driver  
        sampling = random.sample(comments.array, k=tags)
        if tags == 3: 
            comment= sampling[0]+" "+sampling[1]+" "+sampling[2]
        elif tags == 2:
            comment= sampling[0]+" "+sampling[1]
        else:
            comment= sampling[0]

        driver_c.get(link)
        comment_inp = driver_c.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        comment_inp.click()
        comment_inp = driver_c.find_element_by_xpath(
            '/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea')
        comment_inp.clear()
        comment_inp.send_keys(comment)
        comment_post = driver_c.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button')
        comment_post.click()

        return comment
        
os.system('clear')
username = " put username here !!!"
password = " put passwrd here !!!"
repeats = 2 # how many comments ?
account = instagramBot(username, password)
account.login()
time.sleep(8)

for x in range(repeats):
    account.addComment(' put contesst link here !!!',3)# 3 = 3 tags , 2 = 2 tags ,1 = 1 tag - change according to contest rules
     time.sleep(8)
    
account.closeBrowser()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print('Process Successfully Done! time:' , current_time)
        

        
        
        
        
   

