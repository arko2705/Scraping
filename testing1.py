# importing necessary packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import csv
# for holding the resultant list
element_list = []
driver = webdriver.Chrome()
for page in range(1, 3, 1):


    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
    driver.get(page_url)
    title = driver.find_elements(By.CLASS_NAME, "title")
    price = driver.find_elements(By.CLASS_NAME, "price")
    description = driver.find_elements(By.CLASS_NAME, "description")
    rating = driver.find_elements(By.CLASS_NAME, "ratings")

    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

print(element_list)
headings=[["Name","Price","Description","Rating"]]
with open("demofile.csv", "w", newline="") as f:
    
    writer = csv.writer(f)
    writer.writerows(headings)
    writer.writerows(element_list)
print("CSV SAVED")
#closing the driver
driver.close()