import ChromeInstance as CI
import time
import pyautogui
def links():
    cond=True
    while cond:
        try:
            driver=CI.OpeningChrome()
            CI.driver.driver.find_element(By.CLASS_NAME,"HlvSq")#to indicate end to it all
            cond=False
        except:
            pass
        time.sleep(0.1)
        pyautogui.scroll(-300)
    finder=driver.find_elements(By.CLASS_NAME,"hfpxzc") #to find all the links once end reached

if __name__=="__main__":
    links()