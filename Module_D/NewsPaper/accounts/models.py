from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
    
    def update_rating(self):
        from news.models import Post
        from news.models import Comment
        new_rating = 0
        author_posts = Post.objects.filter(author=self)
        author_comments = Comment.objects.filter(user=self.user)
        for post in author_posts:
            new_rating += post.rating * 3
            post_comments = Comment.objects.filter(post=post)
            for comment in post_comments:
                if comment not in author_comments:
                    new_rating += comment.rating
            
        author_comments = Comment.objects.filter(user=self.user)
        for comment in author_comments:
            new_rating += comment.rating

        self.rating = new_rating
        self.save()
    
    def __str__(self):
        return f'{self.user.username}'
