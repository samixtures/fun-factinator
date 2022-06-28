import tweepy
import config
import gspread

# GSPREAD

## Open a google sheet file and sheet1 on that file
gc = gspread.service_account('credentials.json')
wks = gc.open("google api").sheet1


next_tweet = wks.acell('A1').value

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
