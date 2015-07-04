# Shokran

Shokran is a scrapping tool that retrieves all the reviews for any windows phone application.


# Output

The output of the tool is JSON response that would be like this
```javascript

{
  "AppReviews": {
    "Country": [
      {
        "Name": "Egypt",
        "Reviews": {
          "Review": [
            {
              "Author": "Ahmed Kamal",
              "Content": "It is a great app",
              "Date": "2/2/2015",
              "Rating": "5"
            },
            {
              "Author": "Mona Ali",
              "Content": "Nice app",
              "Date": "5/2/2015",
              "Rating": "4"
            }
          ]
        }
      },
      {
        "Name": "United States",
        "Reviews": {
          "Review": [
            {
              "Author": "Mai Anwar",
              "Content": "Silly app",
              "Date": "5/2/2015",
              "Rating": "2"
            },
            {
              "Author": "Mohamed Khaled",
              "Content": "Nice app",
              "Date": "4/2/2015",
              "Rating": "5"
            }
          ]
        }
      }
    ]
  }
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

