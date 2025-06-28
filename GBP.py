import undetected_chromedriver as udc
import search as s
from selenium.webdriver.common.by import By
import time
import pyautogui
from seleniumbase import Driver
import csv

class Logic:
  
    def link_generation(self):##python automatically gives a positional arguement when we call it,so we must write "self"
        googling_it,your_query=s.search()
        driver=udc.Chrome(version_main=137,use_subprocess=False)
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
            if i.get_attribute("href") not in link_list:
                link_list.append(i.get_attribute("href"))
        driver.quit()
        print(f"{len(link_list)} companies found.")
        print("Enter the number of companies you would like to get the information for: ")
        loop_number=input()
        return link_list,your_query,loop_number
       
    def InstanceProvider(self):
       GBPdriver=Driver(uc=True, headless=True,block_images=True)
       emaildriver=Driver(uc=True,headless=True,block_images=True)
       linkedindriver=Driver(uc=True,headless=True,block_images=True)
       return GBPdriver,emaildriver,linkedindriver
    def link_getter(self,i,driver):
        driver.uc_open_with_reconnect(i, reconnect_time=0.1)
        return
    def company(self,i,driven):
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
    def website(self,driver):
           ProbableWebSites=[]
           WebSite=None                  #new concept here
           try:
              WebFinder=driver.find_elements(By.CSS_SELECTOR,".lcr4fd.S9kvJb")
              for g in WebFinder:
                 ProbableWebSites.append(g.get_attribute("href"))
              for h in ProbableWebSites:
                 if h.startswith("http") and not h[-1].isdigit() and not h.startswith("https://api.whatsapp"):
                     WebSite=h
                     break
              if WebSite is None:
                  WebSite="Not present on google business profiles"   
           except:
              WebSite="Not present on google business profiles"
           return WebSite

    def address_PhoneNumber(self,driven):#Gotta fix the address logic by a bit
           try:   
             AFinder=driven.find_element(By.CLASS_NAME,"CsEnBe")
             time.sleep(0.1)
             NeedToClean=AFinder.get_attribute("aria-label")
             Address="Not present on google business profiles"
             if NeedToClean.startswith("Address: "):
                Address=NeedToClean.replace("Address: ","")
           except:
              print("Trouble rendering address")
              Address="Not present on google business profiles"
            
           PFinders=driven.find_elements(By.CSS_SELECTOR,".Io6YTe.fontBodyMedium.kR99db.fdkmkc")
           PhoneNumber="Not present on google business profiles"
           for f in PFinders:
             try: 
                 b=int(f.text.replace(" ",""))+1 
                 PhoneNumber=f.text.replace(" ","")
                 break
             except:
               PhoneNumber="Not present on google business profiles"
           return Address,PhoneNumber
    
    def email(self,Company,Website,driven):
        initial_query="https://www.google.com/search?q="
        if Website and Website.startswith("https") and Website.endswith("/"):
               iweb=Website[:len(Website)-1]
               fweb=iweb.replace("https://","")
               final_query=initial_query+fweb+"+email+address"

        else:       
              OnlyCompany=Company.split('|')
              Company_array=OnlyCompany[0].split(' ')
              for f in Company_array:
                 initial_query=initial_query+"+"+f
              final_query=initial_query+"+email+address"
        try:
            driven.uc_open_with_reconnect(final_query, reconnect_time=0.1)
            driven.find_element(By.XPATH,"//div[@class='sjVJQd pt054b']").click()  ##That give your location prompt that comes up in incognito so that they can give more accurate results
        except:
            pass
        emaillist=[]
        try:
              emailwebelements = driven.find_elements(By.XPATH, "//em[contains(text(),'@')]") 
              for b in emailwebelements:
                  if b.text not in emaillist:
                    emaillist.append(b.text)
        except:
               driven.save_screenshot("email.png")
               emailwebelements="Not found"
        return emaillist
    
    def linkedin(self,Website,Company,driven):
        initial_query="https://www.google.com/search?q="
        if Website and Website.startswith("https") and Website.endswith("/"):
               iweb=Website[:len(Website)-1]
               fweb=iweb.replace("https://","")
               final_query=initial_query+fweb+"+linkedin"

        else:       
              OnlyCompany=Company.split('|')
              Company_array=OnlyCompany[0].split(' ')
              for f in Company_array:
                 initial_query=initial_query+"+"+f
              final_query=initial_query+"+linkedin"
        try:
            driven.uc_open_with_reconnect(final_query, reconnect_time=0.1)
            driven.find_element(By.XPATH,"//div[@class='sjVJQd pt054b']").click()  ##That give your location prompt that comes up in incognito so that they can give more accurate results
        except:
            pass
        linkedin="Could not render"
        try:
              webelement= driven.find_element(By.CLASS_NAME, "zReHs") 
              linkedin=webelement.get_attribute("href")
        except:
               driven.save_element("linkedin.png")
               linkedin="Not found"
        return linkedin


    
    def csv_store(self,element_list,your_query):
        with open(f'ABusiness Profile-{your_query}.csv','w',newline='',encoding='UTF-8') as file: 
            Columns=['Company Name','Address','Phone Number','Google business profile link','Website','E-Mail','Linkedin-Link']
            write=csv.writer(file)
            write.writerow(Columns)
            write.writerows(element_list)
            print("Remember to extend your row width in the csv files,for it to look prettier and better!")