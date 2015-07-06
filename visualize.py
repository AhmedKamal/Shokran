__author__ = 'AhmedKamal'
import plotly.plotly as py
from plotly.graph_objs import *

user_name = 'akamal8'
api_key = 'pn0fsc0htg'

stores_labels = []
stores_reviews_num = []

def visualize_store_reviews(stores):
    for store in stores:
        stores_labels.append(store.store_name)
        stores_reviews_num.append(store.reviews_cnt)

    data = Data(
        [
            Bar(
        x=stores_labels , y =stores_reviews_num
        )
        ])

    plot_url = py.plot(data , filename = 'Stores Reviews Number')
