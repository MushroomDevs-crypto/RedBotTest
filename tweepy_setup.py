import tweepy

# Credentials (Bearer Token)
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIRqxAEAAAAANQXeQNyotFUX7TtmsAE5Lz0wDBI%3DF4p6LvgU2TeKQaAiPSsvazM81QASeh8gLQRo1lvbzOWEfgRu65"

# Conectando à API v2 do Twitter
client = tweepy.Client(bearer_token)

# Criando um tweet usando a API v2
client.create_tweet(text="Hello World")



