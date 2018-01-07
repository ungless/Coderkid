import datetime

from django.shortcuts import render
from django.views import generic
from django.utils import timezone

from . import models

class FourOhFourView(generic.TemplateView):
    template_name = "404.html"

class IndexView(generic.ListView):
    template_name = "almanac/index.html"
    context_object_name = "almanacs"
    queryset = models.Almanac.objects.filter(is_published=True).order_by("-created")

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        margin = datetime.timedelta(days=7)
        new = []
        for almanac in self.queryset:
            if datetime.datetime.today().date() - margin <= almanac.created + margin:
                new.append(almanac.slug)

        context["new"] = new
        return context


class AlmanacView(generic.DetailView):
    template_name = "almanac/detail.html"
    context_object_name = "almanac"
    model = models.Almanac

    def get_queryset(self):
        self.obj = models.Almanac.objects.filter(slug=self.kwargs["slug"])
        return self.obj

    def get_context_data(self, *args, **kwargs):
        context = super(AlmanacView, self).get_context_data(**kwargs)
        context["posts"] = models.Post.objects.filter(almanac=self.get_queryset()[:1], is_published=True).order_by("rank")
        print(context["posts"])
        return context


class PostView(generic.DetailView):
    template_name = "almanac/post.html"
    context_object_name = "post"
    slug_url_kwarg = "post_slug"

    def get_queryset(self):
        self.obj = models.Post.objects.filter(slug=self.kwargs["post_slug"], is_published=True, almanac__slug=self.kwargs["almanac_slug"])
        print(self.obj)
        return self.obj

    def get_context_data(self, *args, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context["examples"] = models.Example.objects.filter(post=self.get_queryset()[:1])
        return context

class ExampleView(generic.DetailView):
    template_name = "almanac/example.html"
    context_object_name = "example"
    slug_url_kwarg = "example_slug"

    def get_queryset(self):
        self.obj = models.Example.objects.filter(slug=self.kwargs["example_slug"], post__is_published=True, post__slug=self.kwargs["post_slug"])
        return self.obj
