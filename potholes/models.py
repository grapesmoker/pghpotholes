import datetime as dt

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.utils import simplejson


class Pothole(models.Model):
    
    lat = models.FloatField()
    long = models.FloatField()
    tweet_id = models.IntegerField()
    reporter_id = models.IntegerField()
    image = models.ImageField()
    image_md5 = models.CharField(max_length=32)
    see_click_fix_url = models.URLField(required=False)
    
    