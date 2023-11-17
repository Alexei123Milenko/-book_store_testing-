import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://practice.automationtesting.in/')

driver.execute_script("window.scrollBy(0, 600);")

driver.get('https://practice.automationtesting.in/product/selenium-ruby/')
REV_btn = driver.find_element_by_css_selector('li.reviews_tab')
REV_btn.click()
star_btn = driver.find_element_by_css_selector('a.star-5')
star_btn.click()
review = driver.find_element_by_css_selector('textarea#comment')
review.click()
review.send_keys('Nice book!')
name = driver.find_element_by_css_selector('input#author')
name.click()
name.send_keys('Max')
em = driver.find_element_by_css_selector('input#email')
em.click()
em.send_keys('123@bc.ru')
sub = driver.find_element_by_css_selector('input#submit.submit')
sub.click()
time.sleep(3)
driver.quit()

