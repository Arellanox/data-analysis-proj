from datetime import datetime
import pandas as pd

covid = pd.read_csv("data/covid19_tweets.csv")
# fecha_primer_tweet = covid['date'].min()
# date_tweet = pd.to_datetime(fecha_primer_tweet)
# hoy = datetime.now()
# hoy = pd.to_datetime(hoy)

def get_dias_transcurridos_por_usuario(usuario):
    subset = covid[covid['user_name']==usuario]
    fecha_primer_tweet = subset['date'].min()
    date_tweet = pd.to_datetime(fecha_primer_tweet)
    hoy = datetime.now()
    hoy = pd.to_datetime(hoy)
    dias_transcurridos = hoy - date_tweet
    return dias_transcurridos
    
# Creamos una lista para conocer todos los usuarios
# usuarios = list()

# llenamos la lista con el usuario unico
# for user in covid['user_name']:
#     if user not in usuarios:
#         usuarios.append(user)

# for user in usuarios:
#     dias = get_dias_transcurridos_por_usuario(user)
#     print(f'Han transcurrido {dias} desde que {user} publicó un tweet')

user = input('Escribe un usuario de tweeter: ')

dias = get_dias_transcurridos_por_usuario(user)
print(f'Han transcurrido {dias} desde que {user} publicó un tweet')
