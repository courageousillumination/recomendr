from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'recomendr.recomendr.views.index', name='recomendr.index'),
    url(r'^courses/(?P<course_id>[0-9]+)', 'recomendr.recomendr.views.course_page', name='recomendr.course_page'),
    url(r'^courses', 'recomendr.recomendr.views.all_courses', name='recomendr.courses')
)
