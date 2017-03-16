from django.conf.urls import url

from bootcamp.feeds import views

urlpatterns = [
    url(r'^$', views.feeds, name='feeds'),
    url(r'^api/comments/', views.FeedCommentsListAPIVIEW.as_view(), name='list'),
    url(r'^api/', views.FeedListAPIView.as_view(), name='list'),
    url(r'^create/', views.FeedCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.FeedDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.FeedUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.FeedDeleteAPIView.as_view(), name='delete'),
    url(r'^post/$', views.post, name='post'),
    url(r'^like/$', views.like, name='like'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^load/$', views.load, name='load'),
    url(r'^check/$', views.check, name='check'),
    url(r'^load_new/$', views.load_new, name='load_new'),
    url(r'^update/$', views.update, name='update'),
    url(r'^track_comments/$', views.track_comments, name='track_comments'),
    url(r'^remove/$', views.remove, name='remove_feed'),
    url(r'^(\d+)/$', views.feed, name='feed'),
]
