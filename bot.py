import gspread
import config
import tweepy

gc = gspread.service_account('credentials.json')

# Open a sheet from a spreadsheet in one go
wks = gc.open("google api").sheet1

# python-api@api-shtuff.iam.gserviceaccount.com
# for x in range(10):
#     wks.update('A', [1, 2])
# wks.update('A1', [[1, 2], [3,4]])

testsite_array = []
with open('facts.txt') as my_file:
    for line in my_file:
        testsite_array.append(line)

# for i in range(1, len(testsite_array)+1):
#     wks.update_cell(i, 1, testsite_array[i-1])

# t = Twitter(
#     auth=OAuth2(bearer_token = config.bearer_token))
    
# print(config.token)

# t.updateStatus("Testing!")

#TWEEPY

client = tweepy.Client(
    # bearer_token=config.bearer_token, 
    consumer_key=config.consumer_key, 
    consumer_secret=config.consumer_secret, 
    access_token=config.acces_token,
    access_token_secret= config.acces_token_secrets,
    # return_type=Response, wait_on_rate_limit=False
    )
    
response = client.create_tweet(text = "Test!")
print(response)