from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'recomendr.recomendr.views.index', name='recomendr.index'),
    url(r'^classes$', 'recomendr.recomendr.views.all_classes', name='recomendr.classes')
)
