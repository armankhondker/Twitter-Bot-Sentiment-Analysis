import tweepy
import csv
from textblob import TextBlob
import re

consumer_key= 'YOUR_KEY'
consumer_secret= 'YOUR_SECRET_CODE'

access_token='YOUR_TOKEN'
access_token_secret='YOUR_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('ANYTHING YOU WANT TO SEARCH ON TWITTER', result_type = 'mixed', count = 100, lang = 'en')
public_tweets1 = api.search('ANYTHING YOU WANT TO SEARCH ON TWITTER', result_type = 'recent', count = 100, lang = 'en')

def clean_tweet( tweet):
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

with open('tweets.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Tweet", "Sentiment Score", "Subjectivity Score"])
    totalSent = 0
    totalSubj = 0
    count = 0 
    for tweet in public_tweets:
        analysis = TextBlob(tweet.text)
        print(tweet.text)
        print(analysis.sentiment)
        print("")
        score = analysis.sentiment.polarity
        subject = analysis.sentiment.subjectivity
        count= count + 1
        totalSent= totalSent + score
        totalSubj= totalSubj + subject
        writer.writerow([clean_tweet(tweet.text), score, subject])
    for tweet in public_tweets1:
        analysis = TextBlob(tweet.text)
        print(tweet.text)
        print(analysis.sentiment)
        print("")
        score = analysis.sentiment.polarity
        subject = analysis.sentiment.subjectivity
        count= count + 1
        totalSent= totalSent + score
        totalSubj= totalSubj + subject
        writer.writerow([clean_tweet(tweet.text), score, subject])
    writer.writerow(['Average Sentmient Score', totalSent/count])
    writer.writerow(['Average Subjectivity Score', totalSubj/count])

print("Logged tweeted sentiments of {0} tweets to tweets.csv".format(len(public_tweets) + len(public_tweets1)))
print("The Average Sentiment Score is {0}".format(totalSent/count))
print("The Average Subjectivity Score is {0}".format(totalSubj/count))
