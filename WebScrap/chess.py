import requests
import bs4
import lxml

req = requests.get("http://books.toscrape.com/")
soup = bs4.BeautifulSoup(req.text,"lxml")
all_content = soup.prettify

# to get class content
class_content = soup.find('div',{'class':'alert alert-warning'})


img = soup.find('img', {'class':'thumbnail'})

# select two rating books title name
two_rating_books = soup.find_all('article', {'class' : 'product_pod'})
two_star = two_rating_books[1]

# select title
title = two_star.select('a')[1]['title']


mylist = []
for i in range(0,20):
    two_star = two_rating_books[i]
    if (two_star.select('.star-rating.Two') != []):
        mylist.append(two_star.select('a')[1]['title'])
    else:
        continue
print(mylist)


