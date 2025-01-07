# Importing Tweepy
import tweepy

# Credentials
api_key = "TO0cePnnznGfc3q1SWZ3u9UMq"
api_secret = "aDIlHS9KLfJMAsuo8jOfw5PlHP4xp064twex2JAscPuvgX3gfW"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAIRqxAEAAAAANQXeQNyotFUX7TtmsAE5Lz0wDBI%3DF4p6LvgU2TeKQaAiPSsvazM81QASeh8gLQRo1lvbzOWEfgRu65"
access_token = "1856858508706418690-kOfhDZ2cTXMlMhQNDywX2BAmzMqAVy"
access_token_secret = "4ci6SA5tnFPnszHkkRuWiwdgj6fLPhzwEplYPpVoi5oU5"

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Creating API instance. This is so we still have access to Twitter API V1 features
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Creating a tweet to test the bot
client.create_tweet(text="Hello World")


