import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get ('https://practice.automationtesting.in/')
time.sleep(3)

shop_btn = driver.find_element_by_css_selector('#menu-item-40')
shop_btn.click()

driver.execute_script("window.scrollBy(0, 300);")

add_to_bascet =  driver.find_element_by_css_selector('[data-product_id="182"]')
add_to_bascet.click()
time.sleep(3)

bascet = driver.find_element_by_css_selector('.wpmenucart-icon-shopping-cart-0')
bascet.click()
time.sleep(3)

# явное ожидание перед нажатием "PROCEED TO CHECKOUT"
proceed_btn = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.button")))
proceed_btn.click()

fn =  driver.find_element_by_css_selector('input#billing_first_name')
fn.send_keys('Max')

Ln = driver.find_element_by_css_selector('input#billing_last_name')
Ln.send_keys('Maxx')

em_ad = driver.find_element_by_css_selector('input#billing_email')
em_ad.send_keys('1234@bc.com')

phone = driver.find_element_by_css_selector('input#billing_phone')
phone.send_keys('123456789')

sel = driver.find_element_by_css_selector('span#select2-chosen-1')
sel.click()

sel_1 = driver.find_element_by_css_selector('input#s2id_autogen1_search')
sel_1.send_keys('Russia')

sel_2 = driver.find_element_by_css_selector('span.select2-match')
sel_2.click()

address = driver.find_element_by_css_selector('input#billing_address_1')
address.send_keys('123')

town = driver.find_element_by_css_selector('input#billing_city.input-text')
town.send_keys('spb')

st = driver.find_element_by_css_selector('input#billing_state.input-text')
st.send_keys('1')

postcode = driver.find_element_by_css_selector('input#billing_postcode.input-text')
postcode.send_keys('2')

driver.execute_script('window.scrollBy(0, 600);')

time.sleep(8)

check_p = driver.find_element_by_css_selector('input#payment_method_cheque')
check_p.click()

place_order = driver.find_element_by_css_selector('input#place_order')
place_order.click()
time.sleep(3)

#проверка, что отображается надпись "Thank you. Your order has been received."
note =  WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element
((By.CSS_SELECTOR,'p.woocommerce-thankyou-order-received'), "Thank you. Your order has been received."))

#проверка, что в Payment Method отображается текст "Check Payments"
pm =  WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element
((By.CSS_SELECTOR, 'li.method'), "Check Payments"))

driver.quit()

