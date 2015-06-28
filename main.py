# -*- coding: utf-8 -*-
__author__ = 'AhmedKamal'

from bs4 import BeautifulSoup
import urllib2

class UserReview:
    def __init__(self , author , content , rating , date):
        self.author = author
        self.content = content
        self.rating = rating
        self.date = date

review_list = []
stores = {}

#get appcode and name from the user
def get_appCode():

    #TODO: get only appid and get the name automatically from any url
    app_code = raw_input('Please Enter your app code which exists at the end of the link')
    app_name = raw_input('Please Enter your app name')
    return  app_code , app_name

#generate urls from different stores
def generate_url_list():
    url_list = []
    app_key , app_name = get_appCode();
    for key in stores:
        store_url = "https://www.windowsphone.com/"+key+"/store/app/"+urllib2.quote(app_name)+"/"+ app_key
        url_list.append(store_url)

    return  url_list

#fill market list dictionary from marketlist file
def get_market_codes():
    reader = open("marketlist" , "r")
    for line in reader:
        tokens = line.split('	')
        stores[tokens[0]] = tokens[1]
    reader.close()
    print(stores)

def get_other_reviews(soup , root_url):

    more_reviews = []
    while(soup.find_all('a' , {"data-ov" : "AppReviews:More reviews"}).__len__() > 0):
        more_link = soup.find_all('a' , {"data-ov" : "AppReviews:More reviews"})[0]['href']
        page_url_hash_start = more_link.index('/reviews?after=')
        more_link = root_url + more_link[page_url_hash_start :]
        req = urllib2.Request(more_link)
        req.add_unredirected_header('User-Agent' , 'Mozilla/5.0')
        newTargetPage = urllib2.urlopen(req)
        soup = BeautifulSoup(newTargetPage.read())
        more_reviews += soup.find_all('li' , {"itemprop" : "review"})
    return more_reviews

def get_reviews(url):
    req = urllib2.Request(url)
    req.add_unredirected_header('User-Agent' , 'Mozilla/5.0')
    print("Debug : " + url)
    #TODO: handle the case when the app may not exist in this store
    try:
        targetPage = urllib2.urlopen(req)
    except urllib2.HTTPError , e:
        print e.code
        print e.msg
        print("The app isnt available in this country")
        return None

    soup = BeautifulSoup(targetPage.read())
    reviews = soup.find_all('li' , {"itemprop" : "review"})

    #get more reviews
    more_reviews = get_other_reviews(soup , url)

    if more_reviews.__len__() > 0:
        ## For Debugging Purposes : print("There are more reviews")
        reviews += more_reviews


    user_reviews = []
    for eachReview in reviews:
        review_author = eachReview.find_all('span' , {"class" : "author noteText"})[0].text
        review_date = eachReview.find_all('span' , {"class" : "date noteText"})[0].text
        review_text = eachReview.find_all('div' , {"itemprop" : "reviewBody"})[0].text
        review_rating = eachReview.find_all('meta' , {"itemprop" : "reviewRating"})[0]['content']
        user_reviews.append(UserReview(review_author , review_text , review_rating , review_date))
    return  user_reviews

#get market code from file
get_market_codes()

#generate different urls for different stores

#for testing purposes
#urls = ['https://www.windowsphone.com/sr-latn-cs/store/app/%D9%82%D9%84-%D8%AD%D9%83%D9%85%D8%A9/6fb0aa74-9f9a-420e-99fe-193c6c278768']

urls = generate_url_list()

#get reviews for each store
for url in urls:
    reviews = get_reviews(url)
    if reviews is None:
        continue

    review_list.append(reviews)
    start = url.index('.com/')
    start += 5
    if url[start:start+10] == 'sr-latn-cs':
        store_code = url[start : start+10]
    else:
        store_code = url[start : start+5]
    print  stores[store_code]+ " " + store_code
    reviews_cnt = reviews.__len__()
    for r in reviews:
        print("Author: " + r.author)
        print("Date: " + r.date)
        print("Content: " + r.content)
        print("Rating: " + r.rating)
        print("\n\n")

    print ("Total Numb of reviews = " + str(reviews_cnt))



