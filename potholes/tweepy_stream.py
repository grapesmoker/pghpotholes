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

# Replace these four fields (i.e. the part that says FIXME)
# with the appropriate date from the twitter dev control
# panel.  
#
# NOTE, OAuth can be used in two ways;
#
# 1) Your app is logging in as 'you' (using your account, or
# perhaps a separate account you create just for this app) and
# so it is rate limited as you (rather than as your IP) and it
# can only access YOUR private data and any public data
#
# 2) Your app is logging in as someone else - i.e you are
# creating an app for other people to use so it needs to
# access their account data.  This is called "Third Party
# OAuth" and is REALLY what OAuth is meant for in the first
# place - but I'm not going to go into that here.
#
# To generate the keys and secrets go to ;
# https://dev.twitter.com/apps/new log in using your account,
# and create an application.  It asks for a Callback URL -
# just leave that blank.  Note that for the 'Your app website'
# URL, you need to include the http:// part of the url or it
# will give you an error about invalid URL format.
#
# After you create your application it'll take you to a page
# where the consumer key and secret are displayed.  Copy and
# paste them below.
consumer_key=''
consumer_secret=''

# At the bottom of the page it says;
#
# Your access token
# 
# It looks like you haven't authorized this application for your own
# Twitter account yet. For your convenience, we give you the opportunity
# to create your OAuth access token here, so you can start signing your
# requests right away. The access token generated will reflect your
# application's current permission level.
#
# Below that is a button, click "Create my Access Token", click it.
#
# A message will appear at the top of the screen for a moment;
#
# Your OAuth access token has been successfully created.  Note that this
# may take a moment to reflect.
# 
# scroll down to the bottom of the page and look for the
# access token and secret - if they aren't there yet, wait a
# bit, reload the page and check again.  Cut and paste them
# into the fields below.
access_token_key = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token_key, access_token_secret)

class TwistStreamListener(tweepy.StreamListener):
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


