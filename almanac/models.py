from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.core.urlresolvers import reverse

class Almanac(models.Model):
    title = models.CharField(max_length=40, unique=True)
    description = models.TextField(max_length=500)
    created = models.DateField(default=timezone.now)
    slug = models.SlugField(editable=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("almanac", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)

        return super(Almanac, self).save(*args, **kwargs)


class Post(models.Model):
    title = models.CharField(max_length=40)
    content = models.TextField()
    slug = models.SlugField(editable=False)
    submitted = models.DateField(default=timezone.now)
    almanac = models.ForeignKey(Almanac, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " (%s)" % self.almanac 

    def get_absolute_url(self):
        return reverse("post", kwargs={"almanac_slug": self.almanac.slug, "post_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)

        return super(Post, self).save(*args, **kwargs)


class Example(models.Model):
    name = models.CharField(max_length=40, unique=True)
    code = models.TextField()
    output = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    language = models.CharField(max_length=40)

    def __str__(self):
        return self.name + " - %s" % self.post 

    def get_absolute_url(self):
        return reverse("example", kwargs={"almanac_slug": self.post.almanac.slug, "post_slug": self.post.slug, "example_slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)

        return super(Example, self).save(*args, **kwargs)
