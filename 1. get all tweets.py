#Twitter Profiler app. This is a simple script to configure the Twitter API
import tweepy, time, csv
#https://github.com/tweepy/tweepy

# Twitter API credentials. Get yours from apps. twitter. com. Twitter acct rquired
# If you need help, visit https: //dev. twitter. com/oauth/overview
consumer_key = "T5khDottNrbUFtVGVtphx09aF"
consumer_secret = "ZAF4ND7GUt9TXbP1eOjp99fTZUjvSKh4n2HS1Hp7rVmdcFfcKY"
access_key = "915590399317639168-cZWmQGXdzDBWgTDHPUltfqWLOA73kxg"
access_secret = "AdydsuSrgyVcfUslkxYanz9oVoyZkz309MPqamdYeXOzS"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
# this function collects a twitter profile request and returns a Twitter object
def get_profile(screen_name):
    try:
        #https: //dev. twitter. com/rest/reference/get/users/show describes get_user
        user_profile = api.get_user(screen_name)
    except:
        user_profile = "Twitter username does not exist"
    return user_profile

# QUESTION 1: Get user input and return unique ID
print ("Please enter a Twitter's username. Ex: tobi is username of Tobi Lütke.")
screen_name = input("Enter your searching username: ")
user = get_profile(screen_name)
print ("")
print ("===============Question 1 of the assignment 3===============")
print ("Fullname is " + user.name + " and Twitter's ID is " + user.id_str)

#this function collects twitter profile tweets and returns Tweet objects
def get_all_tweets(screen_name):
    alltweets = []
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    alltweets.extend(tweets)
    oldest = alltweets[-1].id-1
    while len(tweets) > 0:
              tweets = api.user_timeline(screen_name=screen_name, count=200, max_id=oldest)
              alltweets.extend(tweets)
              oldest = alltweets[-1].id-1
    outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8"), tweet.retweet_count, "\n"] for tweet in alltweets]

    with open ("Shopify_all_tweet.csv", "w") as outfile:
         writer = csv.writer(outfile)
         #writer.writerow(["id","created_at","text"])
         writer.writerow(outtweets)
    pass

screen_name = "CitronResearch"
get_all_tweets(screen_name)
