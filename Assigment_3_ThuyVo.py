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
def get_tweets(screen_name):
    try:
        #https: //developer. twitter. com/en/docs/tweets/timelines/overview descrbes user_timeline
        tweets = api.user_timeline(screen_name=screen_name, count=5200)
    except:
        tweets = "broken"
        # uses the function to query a Twitter user. Try s = get_profile("cd_conrad")
    return tweets

# QUESTION 2: Identify most re-tweeted Tweet from Citron Research
with open ("Citron_most_retweeted.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text", "retweet_count"])
    t = get_tweets("CitronResearch")
    count = 0
    retweet = ''
    print ("")
    print ("===============Question 2 of the assignment 3===============")
    print ("Counting Citron's most retweeted Tweet...")
    for tweet in t:
        if tweet.retweet_count > count:
           count = tweet.retweet_count
           retweet = tweet
    writer.writerow([retweet.id_str, retweet.user.screen_name,retweet.created_at,retweet.text.encode("unicode-escape"), retweet.retweet_count])
    print ("The most retweeted is: "+retweet.text)
    print ("Re-tweet counts = " + str(retweet.retweet_count))

# QUESTION 3:
print ("")
print ("===============Question 3 of the assignment 3===============")
#Create a list of Shopify's Tweets mentions Citron Research
with open ("Shopify_mentions_Citron_Research_and_CitronResearch_mentions_FTC.csv", "w") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(["id","user","created_at","text"])
    t = get_tweets("Shopify")
    count = 0
    keyword = "troll"
    print ("Searching Shopify's Tweets mentioned Citron Research...")
    for tweet in t:
        if keyword in tweet.text:
           count = count + 1
           writer.writerow([tweet.id_str, tweet.user.screen_name,tweet.created_at,tweet.text.encode("unicode-escape")])           
    print (count)

    t = get_tweets("CitronResearch")
    count = 0
    keyword = "FTC"
    print ("Searching CitronResearch's Tweets mentioned FTC...")
    for tweet in t:
        if keyword in tweet.text:
           count = count + 1
           writer.writerow([tweet.id_str, tweet.user.screen_name,tweet.created_at,tweet.text.encode("unicode-escape")])           
    print (count)
