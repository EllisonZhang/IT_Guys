from django.conf.urls import url
from django.contrib import admin
# from "foldername" import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^WeGame$', include('WeGame.urls')),
    url(r'^$', views.index, name='index'),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
