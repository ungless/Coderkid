from django.conf.urls import url
from django.contrib import admin
from almanac import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[-\w]+)/$', views.AlmanacView.as_view(), name="almanac"),
]
