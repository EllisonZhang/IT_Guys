from django.conf.urls import url
from WeGame import views

# app_name = 'WeGame'

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^login/$', views.user_login, name='login'),
    # url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
]