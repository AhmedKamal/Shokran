__author__ = 'AhmedKamal'

from bs4 import BeautifulSoup
import urllib2
#url = "https://www.windowsphone.com/en-eg/store/app/quran-phone/ca503de6-7cef-4ed3-8060-297578729314"
url = "https://www.windowsphone.com/ar-eg/store/app/quran-phone/ca503de6-7cef-4ed3-8060-297578729314"
req = urllib2.Request(url)
req.add_unredirected_header('User-Agent' , 'Mozilla/5.0')
targetPage = urllib2.urlopen(req)
soup = BeautifulSoup(targetPage.read())
#print(soup)
reviews = soup.find_all('li' , {"itemprop" : "review"})
for eachReview in reviews:
    author = eachReview.find_all('span' , {"class" : "author noteText"})[0].text
    date = eachReview.find_all('span' , {"class" : "date noteText"})[0].text
    reviewText = eachReview.find_all('div' , {"itemprop" : "reviewBody"})[0].text
    reviewRating = eachReview.find_all('meta' , {"itemprop" : "reviewRating"})[0]['content']
    print("Author " + author)
    print("Date " + date)
    print("Text " + reviewText)
    print("Rating "+ reviewRating)
    print("\n")