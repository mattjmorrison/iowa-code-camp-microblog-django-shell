from django.conf.urls.defaults import *

urlpatterns = patterns('microblog.views',
    url(r'^$', 'index', name='index'),
    url(r'^save$', 'save', name='save'),
)
