from django.conf.urls.defaults import *

urlpatterns = patterns('microblog.views',
    url(r'^$', 'index', name='index'),
)
