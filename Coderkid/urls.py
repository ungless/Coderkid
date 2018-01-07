from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from almanac import views

handler404 = views.FourOhFourView.as_view()

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('<slug:slug>/', views.AlmanacView.as_view(), name="almanac"),
    path('<slug:almanac_slug>/<slug:post_slug>/', views.PostView.as_view(), name="post"),
    path('<slug:almanac_slug>/<slug:post_slug>/<slug:example_slug>/', views.ExampleView.as_view(), name="example"),
]
