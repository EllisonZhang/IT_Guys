from django.conf.urls import url
from WeGame import views

# app_name = 'WeGame'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^games/(?P<slug>[-\w]+)$', views.GameDetailView.as_view(), name='game_detail'),
    url(r'^games/reviews/new/$', views.ReviewCreateView.as_view(), name='review_new'),
    url(r'^games/reviews/(?P<pk>\d+)/edit/$', views.ReviewUpdateView.as_view(), name='review_edit'),
    url(r'^games/reviews/(?P<pk>\d+)/delete/$', views.ReviewDeleteView.as_view(), name='review_delete'),
    url(r'^about/$', views.about, name='about'),
    url(r'^like/$', views.like_review, name='like_review'),
    url(r'^dislike/$', views.dislike_review, name='dislike_review'),
    url(r'^news/$', views.news, name='news'),
    url(r'^category/$', views.category, name='category'),
    
]