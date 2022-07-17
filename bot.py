import tweepy
import config
import gspread

# GSPREAD

## Open a google sheet file and sheet1 on that file
gc = gspread.service_account('credentials.json')
wks = gc.open("google api").sheet1

#Gets the next tweet from the spreadsheet
next_tweet = wks.acell('A1').value
tweet_length = len(next_tweet) # counts characters of tweet

# Fills testsite_array with each line of facts.txt (41 indices)
if next_tweet == "":
    testsite_array = []
    with open('facts.txt') as my_file:
        for line in my_file:
            testsite_array.append(line)


#TWEEPY

# calling/creating a client to call tweepy methods on
client = tweepy.Client(
    consumer_key=config.consumer_key,
    consumer_secret=config.consumer_secret,
    access_token=config.access_token,
    access_token_secret=config.access_token_secret
)

# If the length of the tweet exceeds the max twitter character count: delete the first row of the spreadsheet
    # and set the "next_tweet" variable to the new first row of the spreadsheet
while tweet_length > 280:
    #Delete the first row so there's a new A1 cell
    wks.delete_rows(1)
    print("New A1 value:", wks.acell('A1').value, sep="\n")
    #Gets the next tweet from the spreadsheet
    next_tweet = wks.acell('A1').value
    tweet_length = len(next_tweet) # counts characters of tweet



#THE ACTUAL CREATION OF THE TWEET
response = client.create_tweet(text=next_tweet)

print("Text we're tweeting (A1 value):", next_tweet, sep="\n")
# print(response)


#GSPREAD
#Delete the first row so there's a new A1 cell
wks.delete_rows(1)
print("New A1 value:", wks.acell('A1').value, sep="\n")


print("checking if statement")

if wks.acell('A1').value == "Done":
    #Creates testsite_array list and adds each line of facts.txt to it
    testsite_array = []
    with open('facts.txt') as my_file:
        for line in my_file:
            testsite_array.append(line)
    #Adds all the values in testsite_array list to the spreadsheet
    for i in range(1, len(testsite_array)+1):
        wks.update_cell(i, 1, testsite_array[i-1])
