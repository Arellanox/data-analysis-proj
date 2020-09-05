import pandas as pd
import matplotlib.pyplot as plt

covid = pd.read_csv("data/covid19_tweets.csv")

def get_tweet_with_link():
   data = covid[covid["text"].str.contains(" | ")].value_counts()
   counter = 0
   for x in data:
       print(x)
       counter+=1
    
   return counter


def get_tweet_with_image():
    data = covid[covid["text"].str.contains("â€¦")]
    counter = 0
    for x in data:
        print(x)
        counter+=1
    
    return counter

tweets_with_links = get_tweet_with_link()
print(f"Existen {tweets_with_links} tweets publicados con LINKS publicados en la base")

tweets_with_image = get_tweet_with_image()
print(f"Existen {tweets_with_image} tweets publicados con IMAGEN publicados en la base")
