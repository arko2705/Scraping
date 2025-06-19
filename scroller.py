import pyautogui
import undetected_chromedriver as udc
from selenium.webdriver.common.by import By
import time

def wow():
    driver=udc.Chrome(use_subprocess=False,)
    driver.get("https://www.google.com/maps/search/ice+cream+shops+near+me/@22.543001,88.3444118,15z/data=!4m2!2m1!6e5?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D")
    pyautogui.click(308,441)
    cond=True
    while cond:
        #print("Enter clicks") 
        #clicks=int(input()) 
        try:
            driver.find_element(By.CLASS_NAME,"HlvSq")
            cond=False
        except:
            pass
        time.sleep(0.1)
        #finder=driver.find_element(By.CSS_SELECTOR,".Io6YTe.fontBodyMedium.kR99db.fdkmkc")
        #print(finder,finder.text)
        pyautogui.scroll(-300)
    driver.quit()
    return 
if __name__=="__main__":
    wow()