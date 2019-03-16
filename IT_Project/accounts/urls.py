from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^signup/', views.SignUpView.as_view(), name='signup'),
]