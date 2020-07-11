import requests as r
import lxml
import bs4

res = r.get("http://www.example.com")
# print(type(res))
# print(res.text)

#------- parsing 

soup = bs4.BeautifulSoup(res.text,"lxml")
# print(soup)
# print(soup.select("p"))  # paragraph content
# print(soup.select("title"))  #Title
# print(soup.select("h1"))
# print(soup.select("h1")[0].getText())   # to get only text

# soup.select by default returns every element as a list.

#print(soup.prettify)
print(soup.title.text)
print(soup.p.text)