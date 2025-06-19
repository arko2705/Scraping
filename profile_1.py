from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui

pyautogui.click(3)
time.sleep(1)
driver=webdriver.Chrome()
time.sleep(1)
pyautogui.hotkey('v')
driver.get('https://www.google.com/search?q=houses+near+me&rlz=1C1ONGR_enIN1070IN1070&oq=houses+near+me&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCDIyMTVqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8')
time.sleep(300)
# import undetected_chromedriver as uc
# import time
# import pyautogui
# import selenium
# options = uc.ChromeOptions()
# driver = uc.Chrome(options=options)

# driver.get("https://www.google.com/maps/search/real+estate+near+me/@22.4897812,88.3570418,13z?entry=ttu&g_ep=EgoyMDI1MDYwOS4wIKXMDSoASAFQAw%3D%3D")
# time.sleep(4)
# pyautogui.position(177,258)
# pyautogui.click()
# time.sleep(10)
# elements=[]
