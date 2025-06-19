from selenium import webdriver
import time
from selenium.webdriver.common.by import By
def emailfinder():
    options=webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver=webdriver.Chrome(options=options)
    Noemaillist=['AI Lead Vision Pvt. Ltd','Skit.ai','Fusion Informatics','Rubixe - AI Company','Ai palette','uniQin.ai','Day One Technologies','DxMinds','DeepBrainz AI & Labs','Mobinius','Observe.AI','Smart AI Technologies - Final year IEEE projects -BE,Mtech,Internship in Bangalore ECE,CSE,IS,EEE','SigTuple']
    emaillist=[]

    for i in Noemaillist:
        initial_query="https://www.google.com/search?q="
        query_list=i.split(" ")
        for f in query_list:
            initial_query=initial_query+"+"+f
        final_query=initial_query+"+email+address"
        driver.implicitly_wait(10)
        driver.get(final_query)
        time.sleep(5)
        #try:
        emaillist.append(driver.find_element(By.CSS_SELECTOR, "div.VwiC3b em").text)
        #except:
        #emaillist.append("Not found")
    print(emaillist)

if __name__=='__main__':
    emailfinder()

