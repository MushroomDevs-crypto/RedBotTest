import tweepy
import os

# Acessando as variáveis de ambiente
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

# Verificando se as credenciais estão sendo carregadas corretamente
if not all([api_key, api_secret, access_token, access_token_secret, bearer_token]):
    raise ValueError("Uma ou mais credenciais não foram configuradas corretamente.")

# Configurando a autenticação OAuth1
auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret
)

# Criando a instância da API com OAuth1
api = tweepy.API(auth)

# Criando a instância do cliente para a API v2
client = tweepy.Client(bearer_token=bearer_token)

# Criando um tweet usando a API v2
client.create_tweet(text="Hello World")


