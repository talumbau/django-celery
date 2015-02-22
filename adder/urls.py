from django.conf.urls import patterns, url

from adder import views

urlpatterns = patterns('',
    # ex: /adder/
    url(r'^$', views.index, name='index'),
    # ex: /adder/show_options/
    url(r'^show_options/$', views.show_options, name='show_options'),
    # ex: /adder/plus_nine/
    url(r'^plus_nine/$', views.plus_nine, name='plus_nine'),
    # ex: /adder/checker/12345/
    url(r'^checker/(?P<async_num>.+)/$', views.checker, name='checker'), 
    # ex: /adder/5/
    url(r'^(?P<result_num>\d+)/$', views.results, name='results'), 
    # ex: /adder/not_ready/
    url(r'^not_ready/(?P<async_num>.+)/$', views.not_ready, name='not_ready'), 
)
