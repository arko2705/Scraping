import requests
import bs4
from seleniumbase import Driver
from selenium.webdriver.common.by import By
import time
# Make two strings with default google search URL
# 'https://google.com/search?q=' and
# our customized search keyword.
# Concatenate them
text= "+AI+Vision+PVT+Email+address"
url = 'https://google.com/search?q=' + text

# Fetch the URL data using requests.get(url),
# store it in a variable, request_result.
#request_result=requests.get( url )
driver = Driver(uc=True, headless=False)
driver.implicitly_wait(5)
driver.uc_open_with_reconnect(url, reconnect_time=6)
try:
 driver.find_element(By.XPATH,"//div[@class='sjVJQd pt054b']").click()
except:
 pass
time.sleep(3)
html=driver.page_source
# Creating soup from the fetched request

soup = bs4.BeautifulSoup(html,
                         "html.parser")#.find_all("em")
print(soup)

#for i in soup:
   # if '@' in i.text:
   #    print(i.text)
print("ended")