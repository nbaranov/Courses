from .models import Post, PostCategory, Comment
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)