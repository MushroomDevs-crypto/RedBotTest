import tweepy
import os


api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

auth = tweepy.OAuth1UserHandler(
    api_key, api_secret, access_token, access_token_secret
)



client = tweepy.Client(bearer_token=bearer_token)

api = tweepy.API(auth)

client.create_tweet(text="Hello World")


