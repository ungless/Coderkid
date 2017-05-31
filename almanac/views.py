from django.shortcuts import render
from django.views import generic
from . import models

class IndexView(generic.ListView):
    template_name = "almanac/index.html"
    context_object_name = "almanacs"
    queryset = models.Almanac.objects.all().order_by("-created")


class AlmanacView(generic.DetailView):
    template_name = "almanac/detail.html"
    context_object_name = "almanac"

    def get_queryset(self):
        self.obj = models.Almanac.objects.filter(slug=self.kwargs["slug"])
        return self.obj

    def get_context_data(self, *args, **kwargs):
        context = super(AlmanacView, self).get_context_data(**kwargs)
        context["posts"] = models.Post.objects.filter(almanac=self.obj)
        return context


class PostView(generic.DetailView):
    template_name = "almanac/post.html"
    context_object_name = "post"
    slug_url_kwarg = "post_slug"

    def get_queryset(self):
        self.obj = models.Almanac.objects.filter(slug=self.kwargs["slug"])
        return self.obj

    def get_context_data(self, *args, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context["examples"] = model.Example.objects.filter(post=self.obj)
        return context

class ExampleView(generic.DetailView):
    pass