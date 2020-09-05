import pandas as pd

covid = pd.read_csv("data/covid19_tweets.csv")

def get_usuarios_por_ciudad():
    data = covid[['user_location','user_name']].groupby("user_location").count()
    return data.head(20)

def tweets_por_usuario():
    data = covid["user_name"].value_counts()
    return data

def top_20_usuario_con_mas_tweets(data):
    data =  data.head(20)
    return data

data = get_usuarios_por_ciudad()
tws = tweets_por_usuario()
users_con_mas_tweets = top_20_usuario_con_mas_tweets(tws)

print("CANTIDAD DE USUARIOS POR CIUDAD")
print(data)
print("USUARIOS CON MAS TWEETS")
print(users_con_mas_tweets)