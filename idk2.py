from bs4 import BeautifulSoup
import requests
from seleniumbase import Driver
def test():
# initialize driver in GUI mode with UC enabled

    driver = Driver(uc=True, headless=True)

    url = "https://www.scrapingcourse.com/cloudflare-challenge"
    driver.uc_open_with_reconnect(url, reconnect_time=6)
    driver.save_screenshot("ucheaedless.png")

if __name__=='__main__':
    test()


