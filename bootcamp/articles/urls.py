from django.conf.urls import url

from bootcamp.articles import views

urlpatterns = [
    url(r'^$', views.articles, name='articles'),
    url(r'^article_api$', views.ArticleListAPIView.as_view(), name='list'),
    url(r'^article_api/(?P<slug>[\w-]+)/$', views.ArticleDetailAPIView.as_view(), name='detail'),
    url(r'^article_api/(?P<slug>[\w-]+)/edit/$', views.ArticleUpdateAPIView.as_view(), name='update'),
    url(r'^article_api/(?P<slug>[\w-]+)/delete/$', views.ArticleDeleteAPIView.as_view(), name='delete'),
    url(r'^write/$', views.write, name='write'),
    url(r'^preview/$', views.preview, name='preview'),
    url(r'^drafts/$', views.drafts, name='drafts'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^tag/(?P<tag_name>.+)/$', views.tag, name='tag'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit_article'),
    url(r'^(?P<slug>[-\w]+)/$', views.article, name='article'),
]
