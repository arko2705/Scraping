from threading import Thread
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import pyautogui # type: ignore
import undetected_chromedriver as udc # type: ignore
import time
from seleniumbase import Driver
import os
import csv
import sys
import search as s
import sys
def main(): 
 Name="Indian School of Ethical Hacking - ISOEH"
 website="www.isoeh.com"
 driver=Driver(uc=True,headless=True)
 driver.implicitly_wait(5)
 driver.uc_open_with_reconnect("https://www.google.com/search?q=Indian+School+of+Ethical+Hacking+-+ISOEH+linkedin",reconnect_time=0.1)
 linkedin="Could not render"
 try:
              webelement= driver.find_element(By.CLASS_NAME, "zReHs") 
              linkedin=webelement.get_attribute("href")
 except:
               driver.save_screenshot("debug.png")
               linkedin="Not found"
 print(linkedin)
 return
if __name__=="__main__":
        main()
