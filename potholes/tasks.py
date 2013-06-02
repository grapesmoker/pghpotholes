import tweepy
#from djcelery import celery
#from models import *

class TwistStreamListener(tweepy.StreamListener):
    
    #def __init__(self):   
    #    super(tweepy.StreamListener, self)
    
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


#@celery.task()

def twist_listener():
    twist = TwistStreamListener()
    
    from thinkathon.auth_data import access_token_key, access_token_secret, consumer_key, consumer_secret
        
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)
    
    hashtag = 'pghpotholes'
    filter_timeout = 60
    sleep_time1 = 6
    sleep_time2 = 60
    
    streaming = tweepy.streaming.Stream(auth, TwistStreamListener(), timeout = twist.filter_timeout)
    print "Starting stream listener to look for hashtag " + hashtag
    queryTerms = [hashtag]
    streaming.filter(follow=None, track=queryTerms)
    
    
    