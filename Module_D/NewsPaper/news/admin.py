from .models import Post, PostCategory, Comment, Author
from django.contrib import admin

# Register your models here.
admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Author)