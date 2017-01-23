from django.conf.urls import url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^api/(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.PostDetail.as_view(), name='post_detail'),
    url(r'^(?P<slug>[-\w]+)/$', views.category_detail, name='category_detail'),
    #url(r'^(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),#
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
