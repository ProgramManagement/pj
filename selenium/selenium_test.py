# -*- coding:utf-8 -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 设置超时时间
driver.maximize_window()  # 窗口最大化显示

#  navigate to the application home page

driver.get("http://127.0.0.1:8000")


search_field = driver.find_element_by_xpath("//a[@href='/user/login/']")
search_field.click()

# enter search keyword and submit
search_field = driver.find_element_by_xpath("//input[@placeholder='请输入用户名']").send_keys("root2")
search_field = driver.find_element_by_xpath("//input[@type='password']").send_keys("11111")
time.sleep(1)
search_field = driver.find_element_by_xpath("//input[@type='submit']").click()

time.sleep(2)

products = driver.find_element_by_xpath("//ul[@class='goods_list fl']//li").click()
products = driver.find_element_by_xpath("//div[@class='operate_btn']//a[1]").click()
time.sleep(1)
products = driver.find_element_by_xpath("//a[@href='javascript:go_order()']").click()
products = driver.find_element_by_xpath("//div[@class='order_submit clearfix']//a[1]").click()
products = driver.find_element_by_xpath("//div[@class='order_submit clearfix']//a[1]").click()


#  close the browser window
time.sleep(3)
driver.quit()

