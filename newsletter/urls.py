from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.IndexView, name='article_list'),
    re_path(r'^article/(?P<pk>\d+)/$', views.DetailView, name='detail'),
    re_path(r'^article/new/$', views.CreateView, name='article_new'),
    re_path(r'^article/(?P<pk>\d+)/edit/$', views.EditView, name='article_edit'),
    re_path(r'^drafts/$', views.DraftsList, name='drafts_list'),
    re_path(r'^article/(?P<pk>\d+)/publish/$', views.PubView, name='publish'),
    re_path(r'^article/(?P<pk>\d+)/remove/$', views.DelView, name='article_delete'),
    re_path(r'^article/(?P<pk>\d+)/comment/$', views.add_comment_to_article, name='add_comment_to_article'),
    re_path(r'^article/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    re_path(r'^article/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
]
