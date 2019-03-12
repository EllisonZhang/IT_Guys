from django.conf.urls import url
from WeGame import views

# app_name = 'WeGame'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^game_detail/$', views.games, name='games'),
    url(r'^games/(?P<pk>\d+)/$', views.GameDetailView.as_view(), name='game_detail'),
    url(r'^games/(?P<pk1>\d+)/reviews/new/$', views.ReviewCreateView.as_view(), name='review_new'),
    url(r'^about/$', views.about, name='about'),
    
]