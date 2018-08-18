from django.conf.urls import url

from . import views

# from .views import PostDetailView, PostsListView


urlpatterns = [
    url(regex=r'^$', view=views.index, name='index'),
    url(regex=r'^article/(?P<id>\d+)/$', view=views.article, name='article'),
    url(regex=r'^fordebug$', view=views.for_debug, name='for_debug'),
    url(regex=r'^about$', view=views.about, name='about'),
    url(regex=r'^register/$', view=views.register, name='register'),
    url(regex=r'^new/$', view=views.new_article, name='new_article'),
    url(regex=r'^my_articles/$', view=views.all_my_articles, name='all_my_articles'),
    url(regex=r'^my_favorites/$', view=views.my_favorites, name='my_favorites'),
]
