from bs4 import BeautifulSoup

soup = BeautifulSoup(open("C:/Users/Megha/Desktop/Storage Estimate1.htm"),'lxml')
content = soup.find('table',{"class":"table"})
items = content.find_all(['td'])
for data in items:
    print(data.get_text())