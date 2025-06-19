import requests
from bs4 import BeautifulSoup
r=requests.get("https://once.com/?ref=onepagelove")
soup=BeautifulSoup(r.content,'html.parser')
s=soup.find('div',class_='page__content')
text=s.find_all('p')
print(text)