from django.contrib import admin

from post.models import Post, PostFile

# Register your models here.
admin.site.register(Post)
admin.site.register(PostFile)
