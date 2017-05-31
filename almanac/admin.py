from django.contrib import admin
from .models import Almanac, Post, Example

admin.site.register(Example)
admin.site.register(Post)
admin.site.register(Almanac)