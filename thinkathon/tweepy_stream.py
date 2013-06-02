import tweepy
from potholes.models import *
# Streaming example using 2 party OAuth 

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
    
        self.hashtag = 'pghpotholes'
        self.filter_timeout = 60
        self.sleep_time1 = 6
        self.sleep_time2 = 60
    
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


def twist_listener():
    twist = TwistStreamListener()
    streaming = tweepy.streaming.Stream(twist.auth, TwistStreamListener(), timeout = twist.filter_timeout)
    print "Starting stream listener to look for hashtag "+hashtag
    queryTerms = [hashtag]
    streaming.filter(follow=None, track=queryTerms)


