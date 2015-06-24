__author__ = 'AhmedKamal'

from bs4 import BeautifulSoup
import urllib2


reviewlist = []
stores = {}

def get_appUrl():
    url = raw_input('Please Enter your app link')
    return  url


def generate_url_list():
    url_list = []
    app_url = get_appUrl();
    for key in stores:
        store_url = "https://www.windowsphone.com/"+key+"/store/app/%D9%82%D9%84-%D8%AD%D9%83%D9%85%D8%A9/6fb0aa74-9f9a-420e-99fe-193c6c278768"
        url_list.append(store_url)
    return  url_list

def get_market_codes():
    reader = open("marketlist" , "r")
    for line in reader:
        tokens = line.split('	')
        stores[tokens[0]] = tokens[1]
    reader.close()
    print(stores)

def get_reviews(url):
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

url = "https://www.windowsphone.com/ar-eg/store/app/%D9%82%D9%84-%D8%AD%D9%83%D9%85%D8%A9/6fb0aa74-9f9a-420e-99fe-193c6c278768"

#get market code from file
get_market_codes()

#generate different urls for different stores
urls = generate_url_list()
print(urls);

#get reviews for each store
for url in urls:
    reviews = get_reviews(url)
    reviewlist.append(reviews)
    start = url.index('.com/')
    start += 5
    store_code = url[start : start+5]
    print  stores[store_code]+ " " + store_code
    print(reviews)

