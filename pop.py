import re
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Coderkid.settings")
import django
django.setup()

from Coderkid.settings import ALMANAC_DIR
from almanac.models import Post, Example, Almanac



posts = []
examples = []

for subdir, dirs, files in os.walk(ALMANAC_DIR):
    for file in files:
        print(subdir)
        print(almanac)
        if not almanac.exists():
            print("DOESNT EXIST")
        print(subdir)
        if dirs == ["examples"]:
            post = Post.objects.filter(slug=subdir.rsplit(ALMANAC_DIR + "/", 1)[1]).values()
            examples.append([os.path.join(subdir, file), file])
        else:
            almanac = Almanac.objects.filter(slug=subdir.rsplit(ALMANAC_DIR + "/", 1)[1]).values()
            posts.append([os.path.join(subdir, file), file[:2], almanac])

for post in posts: 
    print(post)
    file = open(post[0], "r")
    obj = Post(from_file=True, title=post[1].title(), almanac=post[2])
    obj.save()
    file.close()


print(posts)
print(examples)