from django.conf.urls import url

from . import views

# from .views import PostDetailView, PostsListView


urlpatterns = [
    url(regex=r'^$', view=views.index, name='index'),
    # url(regex=r'^(?P<id>\d+)/$', view=views.detail, name='detail'),
    url(regex=r'^article/(?P<id>\d+)/$', view=views.article, name='article'),
    url(regex=r'^fordebug$', view=views.for_debug, name='for_debug'),
    url(regex=r'^about$', view=views.about, name='about'),
]
