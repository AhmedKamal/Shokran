__author__ = 'AhmedKamal'

from bs4 import BeautifulSoup
import urllib2


review_list = []
stores = {}

#get appcode and name from the user
def get_appCode():
    app_code = raw_input('Please Enter your app code which exists at the end of the link')
    app_name = raw_input('Please Enter your app name')
    return  app_code , app_name

#generate urls from different stores
def generate_url_list():
    url_list = []
    app_key , app_name = get_appCode();
    for key in stores:
        store_url = "https://www.windowsphone.com/"+key+"/store/app/"+app_name+"/"+ app_key
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

def get_other_reviews(url):
    req = urllib2.Request(url)
    req.add_unredirected_header('User-Agent' , 'Mozilla/5.0')
    targetPage = urllib2.urlopen(req)
    soup = BeautifulSoup(targetPage.read())
    more_reviews = soup.find_all('li' , {"itemprop" : "review"})
    return more_reviews



def get_reviews(url):
    req = urllib2.Request(url)
    req.add_unredirected_header('User-Agent' , 'Mozilla/5.0')
    print("Debug : " + url)
    #TODO: handle the case when the app may not exist in this store
    targetPage = urllib2.urlopen(req)
    if targetPage.code == 404:
        return
    soup = BeautifulSoup(targetPage.read())
    reviews = soup.find_all('li' , {"itemprop" : "review"})

    #get more reviews
    morePage = soup.find_all('a' , {"data-ov" : "AppReviews:More reviews"})
    more_reviews = get_other_reviews(morePage)
    reviews.append(more_reviews)
    for eachReview in reviews:
        author = eachReview.find_all('span' , {"class" : "author noteText"})[0].text
        date = eachReview.find_all('span' , {"class" : "date noteText"})[0].text
        review_text = eachReview.find_all('div' , {"itemprop" : "reviewBody"})[0].text
        review_rating = eachReview.find_all('meta' , {"itemprop" : "reviewRating"})[0]['content']
        print("Author " + author)
        print("Date " + date)
        print("Text " + review_text)
        print("Rating "+ review_rating)
        print("\n")

#get market code from file
get_market_codes()

#generate different urls for different stores
urls = generate_url_list()

#get reviews for each store
for url in urls:
    reviews = get_reviews(url)
    review_list.append(reviews)
    start = url.index('.com/')
    start += 5
    if url[start:start+10] == 'sr-latn-cs':
        store_code = url[start : start+10]
    else:
        store_code = url[start : start+5]
    print  stores[store_code]+ " " + store_code
    print(reviews)
