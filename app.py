#!/usr/bin/env python3
import platform
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class Facebook:
    def __init__(self,user,password,site_url,path,group_id):
        self.user = user
        self.password = password
        self.site_url = site_url
        self.path = path
        self.group_id = group_id
        self.option = Options()
        self.option.add_experimental_option("prefs", { \
            "profile.default_content_setting_values.media_stream_mic": 1, 
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1, 
            "profile.default_content_setting_values.notifications": 1 
          })
        if platform.system == "windows":
            driver_path = "driver/chromedriver.exe"
        else:
            driver_path = "driver/chromedriver"
    
        self.bot = webdriver.Chrome(options=self.option,executable_path = driver_path)
    def login(self):
        bot = self.bot
        bot.get(self.site_url)
        time.sleep(3)
        user_name = bot.find_element_by_name("email")
        user_name.send_keys(self.user)
        password = bot.find_element_by_name("pass")
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)
        bot.get(self.site_url+self.path+self.group_id)
        time.sleep(3)
        button_xpath = "/html/body/div[1]/div[3]/div[1]/div/div/div/div[2]/span/div[1]/ul/li[1]/a"
        voice_call = bot.find_element_by_xpath(button_xpath)
        voice_call.click()
        time.sleep(1)
        members = bot.find_elements_by_class_name("_4nvn")
        for i in members:
            i.click()
        
        confirm_xpath = "/html/body/div[5]/div[2]/div/div/div/div/div/div/h2/span[2]/button"
        confirm_call = bot.find_element_by_xpath(confirm_xpath)
        confirm_call.click()

def main():
    user = input("Enter Your User ID/Email ")
    password = input("Enter Your Password ")
    site_url = "https://www.facebook.com"
    path = "/messages/t/"
    group_id = "2613328745398719"
    fb = Facebook(user,password,site_url,path,group_id)
    fb.login()

if __name__ == "__main__":
    main()
