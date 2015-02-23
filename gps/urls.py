from django.conf.urls import patterns, include, url

from gps import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'automon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #ex: /gps/
    url(r'^$', views.index, name='index'),
    #ex: /gps/5/
    url(r'^(?P<id>\d+)/$', views.showAll, name='showAll'),
    # ex: /gps/5/update
    url(r'^(?P<id>\d+)/update$', views.update, name='update'),
)
