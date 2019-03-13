from django.conf.urls import url
from WeGame import views

# app_name = 'WeGame'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
<<<<<<< HEAD
    # url(r'^register/$', views.register, name = 'register'),
    # url(r'^login/$', views.login, name='login'),
    # # url(r'^restricted/', views.restricted, name='restricted'),
    # url(r'^logout/$', views.logout, name='logout'),
    url(r'^game_detail/$', views.games, name='games'),
=======
>>>>>>> b5d21417c007d7fdbb1e2ef34a16629bcea15ac8
    url(r'^games/(?P<pk>\d+)/$', views.GameDetailView.as_view(), name='game_detail'),
    url(r'^games/reviews/new/$', views.ReviewCreateView.as_view(), name='review_new'),
    url(r'^games/reviews/(?P<pk>\d+)/edit/$', views.ReviewUpdateView.as_view(), name='review_edit'),
    url(r'^games/reviews/(?P<pk>\d+)/delete/$', views.ReviewDeleteView.as_view(), name='review_delete'),
    url(r'^about/$', views.about, name='about'),
    
]