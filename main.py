from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import pyautogui # type: ignore
import undetected_chromedriver as udc # type: ignore
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import os
import csv
import sys
import search as s
#didnt use beautiful soup,i used selenium cuz google maps is javascript rendered,beautiful soup and requests would haave given back a bs page
def main():
    driver=udc.Chrome(use_subprocess=False,)
    googling_it=s.search()
    driver.get(googling_it)
    print("Enter the number of companies you would like to get the information for: ")
    loop_number=input()
    coordinate=driver.find_element(By.CSS_SELECTOR,".fontTitleLarge.IFMGgb")
    coordinate.click()
    #<generating all the profile links>
    cond=True
    while cond:
        try:
            driver.find_element(By.CLASS_NAME,"HlvSq")#to indicate end to it all
            cond=False
        except:
            pass
        time.sleep(0.05)
        pyautogui.scroll(-400)
    finder=driver.find_elements(By.CLASS_NAME,"hfpxzc") #to find all the links once end reached
    link_list=[]
    for i in finder:
        link_list.append(i.get_attribute("href"))
    driver.quit()
    start=time.time()
    #</generating all the profile links>
    #<Getting the info from the links now>
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driven=webdriver.Chrome(options=options)
    driven.implicitly_wait(5)
    loop_count=0
    element_list=[]
    for i in link_list:#Mostly fixed
     if loop_count<int(loop_number):
       driven.get(i)
       time.sleep(0.3)
       try: 
        CFinder=driven.find_element(By.CSS_SELECTOR, ".m6QErb.Pf6ghf.XiKgde.ecceSd.tLjsW")
        #time.sleep(0.1)
        time.sleep(0.5)
        NeedToStrip=CFinder.get_attribute("aria-label")
        Company=NeedToStrip.replace("Actions for ","")
       except:
         print("Trouble rendering company")
         Company="Not present on google business profiles"

       try:   
         AFinder=driven.find_element(By.CLASS_NAME,"CsEnBe")
         #time.sleep(0.1)
         time.sleep(0.2)
         NeedToClean=AFinder.get_attribute("aria-label")
         Address=NeedToClean.replace("Address: ","")
       except:
         print("Trouble rendering address")
         Address="Not present on google business profiles"
       PFinders=driven.find_elements(By.CSS_SELECTOR,".Io6YTe.fontBodyMedium.kR99db.fdkmkc")
       time.sleep(0.09)
       for f in PFinders:
         try: 
          #a=i.text.replace(" ","")
             b=int(f.text.replace(" ",""))+1 
             PhoneNumber=f.text.replace(" ","")
             break#will have to change.Numbers cant have spaces.Hence number strings with spaces cant be converted to int 
         except:
          PhoneNumber="Not present on google business profiles"
       try:
          WebFinder=driven.find_elements(By.CSS_SELECTOR,".lcr4fd.S9kvJb")
          ProbableWebSites=[]
          for g in WebFinder:
             ProbableWebSites.append(g.get_attribute("href"))
          time.sleep(0.2)
          for h in ProbableWebSites:
             if h.startswith("http") and not h.startswith("https://api.whatsapp"):
                   WebSite=h
                   break
          
       except:
          WebSite="Not present on google business profiles"
          
       condition=True
       for x in element_list:
         if Address in x:
           condition=False
       if condition:
            element_list.append([Company,Address,PhoneNumber,i,WebSite])
            loop_count=loop_count+1
     else:
       break
       
    print(element_list)
    
    end=time.time()
    timeTaken=end-start
    print(f"{timeTaken} seconds taken")

    store_in_csv=input("Store in csv:Yes or no:\n")
    if store_in_csv.lower()=="yes":
      with open(f'Business Profile-{s.your_query}.csv','w',newline='',encoding='UTF-8') as file:  #your_query has to be global to be accessed
        Columns=['Company Name','Address','Phone Number','Google business profile link','Website']
        write=csv.writer(file)
        write.writerow(Columns)
        write.writerows(element_list)
        #3os.startfile(f'Google business profile-{your_query}.csv') 
        print("Remember to extend your row width in the csv files,for it to look prettier and better!")       

    driven.quit()
    return f"Process finished"

if __name__=='__main__':
    main()  