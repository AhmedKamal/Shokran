# Shokran

Shokran is a analytics tool that retrieves all the reviews for any windows phone application in different stores and provide some statistics regarding the app state in market.

# Input

You just need to enter a link to the app like the following app link :
http://windowsphone.com/en-us/store/app/quran-phone/ca503de6-7cef-4ed3-8060-297578729314

# Output

The output of the tool is JSON response that would be like this
```javascript

{
    "app_key": "ca503de6-7cef-4ed3-8060-297578729314",
    "app_name": "quran-phone",
    "store_num": 2,
    "stores_reviews": [
        {
            "average_rating": 5.0,
            "code": "en-CA",
            "reviews": [
                {
                    "author": "by fayaz",
                    "content": "Excellent app would be nice when taping the screen it give two translation \n",
                    "date": "2014-01-19",
                    "rating": "5"
                },
                {
                    "author": "by pholad",
                    "content": "Masha Allah \nThis is indeed an excellent app very useful \nMay Allah reward you abundantly.\nonly Tsfsir ibni kathir needs some review \nBecause some words miss typed  and the بسم الله gets attached with the surah.\nverse search if added would be very helpful jazakallah u khair\nجزاك الله خيرا في الدارين ",
                    "date": "2013-09-27",
                    "rating": "5"
                },
                {
                    "author": "by Mohened",
                    "content": "The Application won't open when selecting an Arabic language from sitting and because of this issue I uninstall it and reinstall it and have the same problem,please fix it,I really like and prefer this great application in Android market.",
                    "date": "2013-09-20",
                    "rating": "5"
                }
            ],
            "reviews_cnt": 3,
            "store_name": "English - Canada"
        },
        {
            "average_rating": 4,
            "code": "ar-SA",
            "reviews": [
                {
                    "author": "بقلم Neji",
                    "content": "سيء جداً .. ما صار يحمل القراءات الصوتية .. يجلس ساااعة يحمل و بعدين يقول معذرةً حصل خطأ ما !! حق الاندرويد أحسن بكثييير ",
                    "date": "15/03/36",
                    "rating": "3"
                },
                {
                    "author": "بقلم محمد",
                    "content": "جميل جزاكم الله خيراً",
                    "date": "24/01/36",
                    "rating": "5"
                }
            ],
            "reviews_cnt": 2,
            "store_name": "Arabic - Saudi Arabia"
        }
    ]
}
```
# Features

- Retrieve All reviews for any windows phone app given its appId and name including 
  * Reviewer Name
  * Review Date
  * User Rating
  * Review Content
  *
- Covers all the markets of windows phone (nearly) with 81 market avaialble.
  


# Requirements

* Install [Python 2.7](https://www.python.org/download/releases/2.7/) 
* Install [Beautiful Soup Library](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup) 


Note : you will find pip installed by default with python 2.7 , so you can just install it using the following command 
```python
pip install beautifulsoup4

