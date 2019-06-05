# @Time: 2019-05-25 15:43
# @Author: 'haifeng.shi@klook.com'


#!/usr/bin/python3
#coding:utf-8
from selenium import webdriver
#下面填入京东的用户名以及密码
jd_up={"ue":"13692818261","pd":"shf00550418"}

chrome=webdriver.Chrome('/Users/klookuser/chromedriver')
chrome.get(url="https://passport.jd.com/new/login.aspx?")
chrome.find_element_by_class_name("login-tab-r").click()
User=chrome.find_element_by_id("loginname")
User.clear()
User.send_keys(jd_up["ue"])
Passwd=chrome.find_element_by_id("nloginpwd")
Passwd.clear()
Passwd.send_keys(jd_up["pd"])
chrome.find_element_by_id("loginsubmit").click()

while True:
    try:
        chrome.get(url="https://cart.jd.com/cart?rd=0.9661885233258125#none")
        # chrome.find_element_by_id("btn-onkeybuy").click()
        chrome.find_element_by_class_name("submit-btn").click()
        print("抢购成功并且已下单！！")
        chrome.quit()
    except Exception:
        break
        print("还未开始抢购！！")

#
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome('/Users/klookuser/chromedriver')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/xhtml');
# # time.sleep(5) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# # time.sleep(5) # Let the user actually see something!
# driver.quit()

# import time
#
# from selenium import webdriver
# import selenium.webdriver.chrome.service as service
#
# service = service.Service('/Users/klookuser/chromedriver')
# service.start()
# capabilities = {'chrome.binary': '/path/to/custom/chrome'}
# print(service.service_url)
# driver = webdriver.Remote(service.service_url, capabilities)
# driver.get('http://www.google.com/xhtml');
# time.sleep(5) # Let the user actually see something!
# driver.quit()