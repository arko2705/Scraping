from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
def main():
  service = Service(ChromeDriverManager().install())
  driver = webdriver.Chrome(service=service)
if __name__=="__main__":
  main()