from seleniumbase import Driver
from selenium.webdriver.common.by import By
def idk():
    driver=Driver(uc=True,headless=True)
    driver.uc_open_with_reconnect("https://www.google.com/maps/place/CSA+Consultants+Private+Limited/@22.5270536,88.1999993,12z/data=!4m10!1m2!2m1!1sconsulting+companies+in+kolkata!3m6!1s0x3a0277301a1702e9:0x494bf3bca372e6dd!8m2!3d22.5270536!4d88.3524346!15sCh9jb25zdWx0aW5nIGNvbXBhbmllcyBpbiBrb2xrYXRhWiEiH2NvbnN1bHRpbmcgY29tcGFuaWVzIGluIGtvbGthdGGSARBzb2Z0d2FyZV9jb21wYW55mgEjQ2haRFNVaE5NRzluUzBWSlEwRm5TVVJDZUdWbWRFVkJFQUWqAW0KCS9tLzAybjlqdhABKhgiFGNvbnN1bHRpbmcgY29tcGFuaWVzKAAyHxABIhu8T5JwfPAT_MDs8-ZgLRcP91thjexM1ZfLHEoyIxACIh9jb25zdWx0aW5nIGNvbXBhbmllcyBpbiBrb2xrYXRh4AEA-gEECAAQMw!16s%2Fg%2F11cm0_l4w1?entry=ttu&g_ep=EgoyMDI1MDYxNy4wIKXMDSoASAFQAw%3D%3D",reconnect_time=0)
    driver.find_element(By.CSS_SELECTOR, ".m6QErb.Pf6ghf.XiKgde.ecceSd.tLjsW")
    NeedToStrip=driver.get_attribute("aria-label")
    Company=NeedToStrip.replace("Actions for ","")
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
    return WebSite,Company
def main():
     print(idk())
if __name__=="__main__":
     main()