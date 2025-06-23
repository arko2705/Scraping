import threading
from selenium import webdriver # type: ignore
from selenium.webdriver.common.by import By # type: ignore
import pyautogui # type: ignore
import undetected_chromedriver as udc # type: ignore
import time
from seleniumbase import Driver
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
import os
import csv
import sys
import search as s
import sys
#didnt use beautiful soup,i used selenium cuz google maps is javascript rendered,beautiful soup and requests would haave given back a bs page
class Logic:
  
    def link_generation(self):##python automatically gives a positional arguement when we call it,so we must write "self"
        driver=udc.Chrome(use_subprocess=False,)
        googling_it,your_query=s.search()
        driver.get(googling_it)
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
        print("Enter the number of companies you would like to get the information for: ")
        loop_number=input()
        driver.quit()
        return link_list,your_query,loop_number
       
    def InstanceProvider(self):
       driven=Driver(uc=True, headless=True)
       return driven
    
    def company(self,i,driven):
           driven.uc_open_with_reconnect(i, reconnect_time=0.1)
           time.sleep(0.3)
           try: 
            CFinder=driven.find_element(By.CSS_SELECTOR, ".m6QErb.Pf6ghf.XiKgde.ecceSd.tLjsW")
            time.sleep(0.1)
            NeedToStrip=CFinder.get_attribute("aria-label")
            Company=NeedToStrip.replace("Actions for ","")
           except:
             print("Trouble rendering company")
             Company="Not present on google business profiles"
           return Company
   
    def address_PhoneNumber_website(self,driven):
           try:   
             AFinder=driven.find_element(By.CLASS_NAME,"CsEnBe")
             time.sleep(0.1)
             NeedToClean=AFinder.get_attribute("aria-label")
             Address=NeedToClean.replace("Address: ","")
           except:
              print("Trouble rendering address")
              Address="Not present on google business profiles"
            
           PFinders=driven.find_elements(By.CSS_SELECTOR,".Io6YTe.fontBodyMedium.kR99db.fdkmkc")
           for f in PFinders:
             try: 
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
              for h in ProbableWebSites:
                 if h.startswith("http") and not h[-1].isdigit() and not h.startswith("https://api.whatsapp"):
                     WebSite=h
                     break
           except:
              WebSite="Not present on google business profiles"
           return Address,PhoneNumber,WebSite
    
    def email(self,Company,driven):
           try:
              OnlyCompany=Company.split('|')
              Company_array=OnlyCompany[0].split(' ')
              initial_query="https://www.google.com/search?q="
              for f in Company_array:
                 initial_query=initial_query+"+"+f
              final_query=initial_query+"+email+address"
              driven.uc_open_with_reconnect(final_query, reconnect_time=0.1)
              driven.find_element(By.XPATH,"//div[@class='sjVJQd pt054b']").click()  ##That give your location prompt that comes up in incognito so that they can give more accurate results
           except:
               pass
           try:
              emailwebelements = driven.find_elements(By.XPATH, "//em[contains(text(),'@')]") 
              emaillist=[]
              for b in emailwebelements:
                  emaillist.append(b.text)
           except:
               driven.save_screenshot("debug.png")
               emailwebelements="Not found"
           return emaillist
    
    def csv_store(self,element_list,your_query):
        with open(f'iBusiness Profile-{your_query}.csv','w',newline='',encoding='UTF-8') as file: 
            Columns=['Company Name','Address','Phone Number','Google business profile link','Website','E-Mail']
            write=csv.writer(file)
            write.writerow(Columns)
            write.writerows(element_list)
            print("Remember to extend your row width in the csv files,for it to look prettier and better!")

def main():
   logic=Logic()
   link_list,your_query,loop_number=logic.link_generation()
   driven=logic.InstanceProvider()
   driven.implicitly_wait(5)
   start=time.time()
   loop_count=0
   element_list=[]
   for i in link_list:
      if loop_count<int(loop_number):
         Company=logic.company(i,driven)
         Address,PhoneNumber,Website=logic.address_PhoneNumber_website(driven)
         map_link=i
         emaillist=logic.email(Company,driven)
         element_list.append(Company,Address,PhoneNumber,map_link,Website)
      else:
         driven.quit()
         break
   print(element_list)
   end=time.time()
   print(f"{end-start} seconds taken")
   store_in_csv=input("Store in csv:Yes or no:\n")
   if store_in_csv.lower()=="yes":
       logic.csv_store(element_list,your_query)
  
if __name__=='__main__':
    main()  
