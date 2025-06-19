from selenium import webdriver
from selenium.webdriver.common.by import By
import undetected_chromedriver as udc
import time
import csv
import pyautogui
def test():
    driver=udc.Chrome(use_subprocess=False,)
    driver.get("https://www.google.com/maps/search/digital+marketing+companies+in+kolkata/@22.5987975,88.3832932,13z?entry=ttu&g_ep=EgoyMDI1MDYxMS4wIKXMDSoASAFQAw%3D%3D")
    pyautogui.click(308,441)
    cond=True
    while cond:
        try:
            driver.find_element(By.CLASS_NAME,"HlvSq")
            cond=False
        except:
            pass
        time.sleep(0.1)
        pyautogui.scroll(-300)
    finder=driver.find_elements(By.CLASS_NAME,"hfpxzc") 
    link_list=[]
    for i in finder:
        link_list.append(i.get_attribute("href"))

    #number=input("Enter the number of companies you want information for:\n")
    loop_count=0
    element_list=[]
    for i in link_list:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        driven=webdriver.Chrome(options=options)
        driven.get(i)
        time.sleep(0.2)
        try: 
            finding=driver.find_element(By.CSS_SELECTOR, ".hh2c6.G7m0Af")
            NeedToStrip=finding.get_attribute("aria-label")
            time.sleep(0.3)
            Company=NeedToStrip.replace("Overview of ","")
        except:
            print("Trouble rendering company")#I tried for 70 profiles.Around 6-7/70 values were missed
            Company="Not present on google business profiles"

        try:   
            find=driver.find_element(By.CLASS_NAME,"CsEnBe")
            time.sleep(0.3)
            Address=find.get_attribute("aria-label")
        except:
            print("Trouble rendering address")
            Address="Not present on google business profiles"
        finders=driver.find_elements(By.CSS_SELECTOR,".Io6YTe.fontBodyMedium.kR99db.fdkmkc")
        time.sleep(0.3)
        for i in finders:
             try: 
              a=i.text.replace(" ","")
              b=int(a)+1 
              PhoneNumber=i.text
              break#will have to change.Numbers cant have spaces.Hence number strings with spaces cant be converted to int 
          #if len(i.text)==12:#is also flawed,cuz for one result there was "Find a table" which matches 12 characters.So gotta change this too.
           #PhoneNumber=i.text
           #break
          #else:
           # PhoneNumber="No Value"

             except:
              PhoneNumber="Not present on google business profiles"
        condition=True
        for x in element_list:
            if Company in x:
               condition=False
        if condition==True:
            element_list.append([Company,Address,PhoneNumber])
            loop_count=loop_count+1
    store_in_csv=input("Store in csv:Yes or no:\n")
    if store_in_csv.lower()=="yes":
      with open(f'Business Profile-{your_query}.csv','w',newline='') as file:
        Columns=['Company Name','Address','Phone Number']
        write=csv.writer(file)
        write.writerow(Columns)
        write.writerows(element_list)

if __name__=='__main__':
   test()

    

