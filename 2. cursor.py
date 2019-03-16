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
def get_tweets(screen_name):
    alltweets = []
    for tweets in tweepy.Cursor(api.user_timeline, screen_name="CitronResearch").items(100):
        alltweets.extend(tweets)
        with open ("Citron_most_retweeted.csv", "w") as outfile:
             writer = csv.writer(outfile)
             #writer.writerow(["id","user","created_at","text", "retweet_count"])
             #writer.writerow([tweets.id_str, tweets.user.screen_name,tweets.created_at,tweets.text.encode("unicode-escape"), tweets.retweet_count])
             writer.writerow([alltweets])
screen_name = "CitronResearch"
get_tweets(screen_name)
