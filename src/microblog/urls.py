from django.conf.urls.defaults import *

urlpatterns = patterns('microblog.views',
    url(r'^$', 'index', name='index'),
    url(r'^save/$', 'save_message', name='save_message'),
)
