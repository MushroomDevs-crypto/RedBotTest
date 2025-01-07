import tweepy
import os

# Obtendo o Bearer Token da variável de ambiente
bearer_token = os.getenv("BEARER_TOKEN")

# Conectando à API v2
client = tweepy.Client(bearer_token)

# Criando um tweet
client.create_tweet(text="Hello World")



