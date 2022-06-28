import tweepy
import config

# calling a client
client = tweepy.Client(
    consumer_key=config.consumer_key,
    consumer_secret=config.consumer_secret,
    access_token=config.access_token,
    access_token_secret=config.access_token_secret
)

response = client.create_tweet(text='twitter api testoooor')


print(response)