import pandas as pd
import matplotlib.pyplot as plt

covid = pd.read_csv("data/covid19_tweets.csv")

# def get_tweets_por_ciudad(city):
#     counter = 0
#     for x in covid['user_location'].head(4):
#         if x == city:
#             counter+=1
    
#     return counter

# def dibujar_grafica(data):
#     data.plot()

# ciudades_list = list()

# for ciudad in covid['user_location'].head(4):
#     if ciudad not in ciudades_list:
#         ciudades_list.append(ciudad)

# grafica = list()

# for ciudad in ciudades_list:
#     tweets = get_tweets_por_ciudad(ciudad)
#     grafica.append({"ciudad": ciudad, "tweets": tweets})

# print(grafica)

def get_cantidad_tweets_por_ciudad():
    data = covid["user_location"].head(20).value_counts()
    return data

def dibujar_grafica(data):
    data.plot.bar()


tws = get_cantidad_tweets_por_ciudad()

dibujar_grafica(tws)