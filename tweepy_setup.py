import tweepy

# Credentials (Bearer Token)
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
access_token = "YOUR_ACCESS_TOKEN"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
bearer_token = "YOUR_BEARER_TOKEN"


# Conectando à API v2 do Twitter
client = tweepy.Client(bearer_token)

# Criando um tweet usando a API v2
client.create_tweet(text="Hello World")



