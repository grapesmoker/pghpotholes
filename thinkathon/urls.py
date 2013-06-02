from django.conf.urls import patterns, include, url
from potholes.views import *

from potholes import tasks
from threading import Thread

print 'fooo'

twitter_thread = Thread(target=tasks.twist_listener)
twitter_thread.setDaemon(True)
twitter_thread.start()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'thinkathon.views.home', name='home'),
    # url(r'^thinkathon/', include('thinkathon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^thinkathon/$', main),
    url(r'^$', main),
    url(r'^getdata/$', getdata),
)
