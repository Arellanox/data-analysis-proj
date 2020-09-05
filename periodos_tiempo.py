import pandas as pd
import matplotlib.pyplot as plt

covid = pd.read_csv("data/covid19_tweets.csv")

# convertimos a tiempo la columna date
covid["date"] = pd.to_datetime(covid["date"])

# agrego la columna de mes al dataframe

covid['month'] = covid['date'].dt.month

def get_tweets_por_mes():
    data = covid["month"].value_counts()
    return data


def get_tweets_por_semana():
    data = covid["week"].value_counts()
    return data


def get_tweets_por_hora():
    data = covid["hour"].value_counts()
    return data


def get_tweets_por_categoria():
    data = covid["categoria"].value_counts()
    mayor = data.max()
    return data

tweets_por_mes = get_tweets_por_mes()

print("Cantidad de tweets por mes")
print(tweets_por_mes)

covid["week"] = covid["date"].dt.week


tweets_por_semana = get_tweets_por_semana()
print("Cantidad de tweets por semana")
print(tweets_por_semana)

covid["hour"] = covid["date"].dt.hour


tweets_por_hora = get_tweets_por_hora()
print("Cantidad de tweets por hora")
print(tweets_por_hora)

bins = [-1,11,18,23]
categoria = ["Morning","afternoon","nigth"]

covid["categoria"] = pd.cut(covid["hour"],bins,labels=categoria)

categoria_con_mas_tweets = get_tweets_por_categoria()
print(categoria_con_mas_tweets)