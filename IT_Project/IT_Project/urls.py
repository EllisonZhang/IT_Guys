from django.conf.urls import url
from django.contrib import admin
from WeGame import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^WeGame$',  include('WeGame.urls')),
    url(r'^$', views.index, name='index'),
    # url(r'^accounts/', include('registration.backends.simple.urls')),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
