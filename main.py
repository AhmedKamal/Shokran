# -*- coding: utf-8 -*-
__author__ = 'AhmedKamal'

from bs4 import BeautifulSoup
import urllib2
import json
import visualize
from json import JSONEncoder


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class UserReview:
    def __init__(self, author, content, rating, date):
        self.author = author
        self.content = content
        self.rating = rating
        self.date = date


class Store:
    def __init__(self, code, store_name, reviews_cnt, average_rating, reviews):
        self.code = code
        self.store_name = store_name
        self.reviews_cnt = reviews_cnt
        self.average_rating = average_rating
        self.reviews = reviews


class Application:
    def __init__(self, app_name, app_key, store_num, stores_reviews):
        self.app_name = app_name
        self.store_num = store_num
        self.app_key = app_key
        self.stores_reviews = stores_reviews


review_list = []
stores = {}
app_name = ''
app_key = ''
# get appcode and name from the user
def get_appCode():
    #TODO: get only appid and get the name automatically from any url
    global app_name, app_key
    key = raw_input('Please Enter your app code which exists at the end of the link')
    name = raw_input('Please Enter your app name')
    app_name = name
    app_key = key


#generate urls from different stores
def generate_url_list():
    global app_name, app_key
    url_list = []
    get_appCode();
    for key in stores:
        store_url = "https://www.windowsphone.com/" + key + "/store/app/" + urllib2.quote(app_name) + "/" + app_key
        url_list.append(store_url)

    return url_list


#fill market list dictionary from marketlist file
def get_market_codes():
    reader = open("marketlist", "r")
    for line in reader:
        tokens = line.split('	')
        stores[tokens[0]] = tokens[1]
    reader.close()
    print(stores)


def get_other_reviews(soup, root_url):
    more_reviews = []
    while (soup.find_all('a', {"data-ov": "AppReviews:More reviews"}).__len__() > 0):
        more_link = soup.find_all('a', {"data-ov": "AppReviews:More reviews"})[0]['href']
        page_url_hash_start = more_link.index('/reviews?after=')
        more_link = root_url + more_link[page_url_hash_start:]
        req = urllib2.Request(more_link)
        req.add_unredirected_header('User-Agent', 'Mozilla/5.0')
        newTargetPage = urllib2.urlopen(req)
        soup = BeautifulSoup(newTargetPage.read())
        more_reviews += soup.find_all('li', {"itemprop": "review"})
    return more_reviews


def get_reviews(url):
    req = urllib2.Request(url)
    req.add_unredirected_header('User-Agent', 'Mozilla/5.0')
    print("Debug : " + url)
    #TODO: handle the case when the app may not exist in this store
    try:
        targetPage = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.code
        print e.msg
        print("The app isnt available in this country")
        return None

    soup = BeautifulSoup(targetPage.read())
    reviews = soup.find_all('li', {"itemprop": "review"})

    #get more reviews
    more_reviews = get_other_reviews(soup, url)

    if more_reviews.__len__() > 0:
        ## For Debugging Purposes : print("There are more reviews")
        reviews += more_reviews

    user_reviews = []
    for eachReview in reviews:
        review_author = eachReview.find_all('span', {"class": "author noteText"})[0].text
        review_date = eachReview.find_all('span', {"class": "date noteText"})[0].text
        review_text = eachReview.find_all('div', {"itemprop": "reviewBody"})[0].text
        review_rating = eachReview.find_all('meta', {"itemprop": "reviewRating"})[0]['content']
        user_reviews.append(UserReview(review_author, review_text, review_rating, review_date))
    return user_reviews


def get_average_rating(reviews):
    rating_sum = 0
    for review in reviews:
        rating_sum += float(review.rating)
    return rating_sum / reviews.__len__()

#get market code from file
get_market_codes()

#generate different urls for different stores

#for testing purposes
# urls = [
#       'https://www.windowsphone.com/ar-EG/store/app/%D8%B2%D9%85%D9%84%D9%83%D8%A7%D9%88%D9%8A/57c19208-fff9-4370-963a-4206ca5e3e87',
#       'https://www.windowsphone.com/en-ca/store/app/%D8%B2%D9%85%D9%84%D9%83%D8%A7%D9%88%D9%8A/57c19208-fff9-4370-963a-4206ca5e3e87',
#       'https://www.windowsphone.com/ar-SA/store/app/%D8%B2%D9%85%D9%84%D9%83%D8%A7%D9%88%D9%8A/57c19208-fff9-4370-963a-4206ca5e3e87']

urls = generate_url_list()

#get reviews for each store
app_reviews = []
current_store = None

for url in urls:
    reviews = get_reviews(url)
    if reviews.__len__() == 0:
        continue
    review_list.append(reviews)
    start = url.index('.com/')
    start += 5
    if url[start:start + 10] == 'sr-latn-cs':
        store_code = url[start: start + 10]
    else:
        store_code = url[start: start + 5]

    reviews_cnt = reviews.__len__()

    average_rating = get_average_rating(reviews)

    current_store = Store(store_code, stores[store_code], reviews_cnt, average_rating, reviews)
    app_reviews.append(current_store)

#print json data about the app including reviews , average , rating for each store , .. etc
app = Application(app_name, app_key, app_reviews.__len__(), app_reviews)
json_resp = json.dumps(app, indent=4, sort_keys=True, cls=MyEncoder, ensure_ascii=False)
visualize.visualize_store_reviews(app_reviews)
print json_resp


