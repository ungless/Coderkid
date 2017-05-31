from django.shortcuts import render
from django.views import generic
from . import models

class IndexView(generic.ListView):
    template_name = "almanac/index.html"
    context_object_name = "almanacs"
    queryset = models.Almanac.objects.all().order_by("-created")


class AlmanacView(generic.DetailView):
    template_name = "almanac/detail.html"
    model = models.Almanac
    context_object_name = "almanac"