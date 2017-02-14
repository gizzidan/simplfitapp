from django.conf.urls import url
from . import views
from .views import PostMonthArchiveView, PostWeekArchiveView

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<pk>\d+)-(?P<slug>[-\w]+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<slug>[-\w]+)/$', views.category_detail, name='category_detail'),
    url(r'^new/$', views.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[-\w]+)/$',
        PostMonthArchiveView.as_view(),
        name="archive_month"),
    url(r'^(?P<year>[0-9]{4})/week/(?P<week>[0-9]+)/$',
        PostWeekArchiveView.as_view(),
        name="archive_week"),
]
