from django.conf.urls import url
from django.contrib import admin
from almanac import views

handler404 = views.FourOhFourView.as_view()

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^admin/', admin.site.urls),
    url(r'^(?P<slug>[-\w]+)/$', views.AlmanacView.as_view(), name="almanac"),
    url(r'^(?P<almanac_slug>[-\w]+)/(?P<post_slug>[-\w]+)/$', views.PostView.as_view(), name="post"),
    url(r'^(?P<almanac_slug>[-\w]+)/(?P<post_slug>[-\w]+)/(?P<example_slug>[-\w]+)$', views.ExampleView.as_view(), name="example"),
]

