from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'recomendr.recomendr.views.index', name='index'),
)
