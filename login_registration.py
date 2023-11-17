import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

MyAc_btn = driver.find_element_by_link_text('My Account')
MyAc_btn.click()

us = driver.find_element_by_css_selector(' input#username')
us.send_keys('123@bc.ru')
pas = driver.find_element_by_css_selector('input#password')
pas.send_keys('555MMMnnn-12')

log_btn = driver.find_element_by_css_selector('[value="Login"]')
log_btn.click()

elementLogout = driver.find_element_by_link_text("Logout")
driver.quit()

