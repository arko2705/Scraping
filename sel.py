# import webdriver 
from selenium import webdriver 

# create webdriver object 
driver = webdriver.FireFox()

# get google.co.in 
driver.get("https://google.co.in/search?q=geeksforgeeks")