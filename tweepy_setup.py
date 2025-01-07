import tweepy
import os

# Acessando as variáveis de ambiente
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Configurando a autenticação OAuth1
auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret
)

# Criando a instância da API
api = tweepy.API(auth)

# Criando a instância do cliente para a API v2
client = tweepy.Client(bearer_token=os.getenv("BEARER_TOKEN"))

# Criando um tweet usando a API v2
client.create_tweet(text="Hello World")


