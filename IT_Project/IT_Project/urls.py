from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from WeGame import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^wegame/',  include('WeGame.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^$', views.index, name='index'),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
