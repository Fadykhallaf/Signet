from django.conf.urls import url
from bootcamp.communities import views

urlpatterns = [
    url(r'^$', views.pickupCommunity, name='community'),
    url(r'^api/', views.CommunityListAPIView.as_view()),
    url(r'^vote/$', views.vote, name='vote'),
]
