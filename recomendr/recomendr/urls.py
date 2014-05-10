from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'recomendr.recomendr.views.index', name='recomendr.index'),
    url(r'^courses/(?P<course_id>[0-9]+)', 'recomendr.recomendr.views.course_page', name='recomendr.course_page'),
    url(r'^courses', 'recomendr.recomendr.views.all_courses', name='recomendr.courses'),
    url(r'^search', 'recomendr.recomendr.views.search', name='recomendr.search'),
    url(r'^random', 'recomendr.recomendr.views.random_course', name='recomendr.random_course'),
    url(r'^my_courses', 'recomendr.recomendr.views.my_courses', name='recomendr.my_courses'),
)
