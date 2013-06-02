import sys
import tweepy
from pprint import pprint
import time
import os
import shelve
import csv

# Streaming example using 2 party OAuth 


# turn off output buffering on stdout
sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

#hashtag="pghpotholessean"
hashtag="pghpotholes"
FILTER_TIMEOUT = 60
SLEEP_TIME1 = 6
SLEEP_TIME2 = 60

class TwistStreamListener(tweepy.StreamListener):
    
    def __init__(self):
        super(tweepy.StreamListener, self)
        from thinkathon.auth_data import access_token_key, access_token_secret, consumer_key, consumer_secret
        self.access_token_key = access_token_key
        self.access_token_secret = access_token_secret
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token_key, self.access_token_secret)
    
    def on_status(self, status):
        try:
            print "%s\t%s\t%s\t%s" % (status.text, 
                                      status.author.screen_name, 
                                      status.created_at, 
                                      status.source,)
        except Exception, e:
            print 'Exception:', e
            pass


    def on_error(self, status_code):
        print 'Error, status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print 'Timeout.'
        return True # Don't kill the stream


twist = TwistStreamListener()
streaming = tweepy.streaming.Stream(auth, TwistStreamListener(), timeout = FILTER_TIMEOUT)
print "Starting stream listener to look for hashtag "+hashtag
queryTerms = [hashtag]
streaming.filter(follow=None, track=queryTerms)

print "Twist is existing."


