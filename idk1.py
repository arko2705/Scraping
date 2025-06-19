from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as udc
from seleniumbase import Driver
import time
def damn():
    bruh='keyline '
    ayo=bruh.split(' ')
    initial_query="https://www.google.com/search?q="
    for f in ayo:
       initial_query=initial_query+"+"+f
    final_query=initial_query+"+email+address"
    driver = Driver(uc=True, headless=True)
    driver.implicitly_wait(5)
    driver.uc_open_with_reconnect(final_query, reconnect_time=6)
    try:
        driver.find_element(By.XPATH,"//div[@class='sjVJQd pt054b']").click()
    except:
       pass
    driver.save_screenshot("yoheadless.png")
    
    
    try:
     email = driver.find_elements(By.XPATH, "//div[contains(@class,'VwiC3b')]/span/em[contains(text(),'@')]") 
    except:
        email="Not found"
    for i in email:
       print(i.text.)

if __name__=='__main__':
    damn()
