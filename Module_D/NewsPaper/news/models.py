from django.db import models
from django.contrib.auth.models import User
from accounts.models import Author
from datetime import datetime



class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    post = "PS"
    news = "NW"
    TYPE = [
        (post, "Статья"),
        (news, "Новость"),
    ]
    author = models.ForeignKey(Author,
                               on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=TYPE, default=post)
    create_time = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, through="PostCategory")
    header = models.CharField(max_length=256, 
                              default='Заголовок отсутвует')
    text = models.TextField(default='Текст отсутствует')
    rating = models.FloatField(default=0.0)
    
    def like(self):
        self.rating += 1
        
    def dislike(self):
        self.rating -= 1   
    
    def preview(self):
        return f'{self.text[:256]} ... '
    
    def __str__(self):
        return f'{self.preview()}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def  __str__ (self):
        return f'{self.category.name}'
        


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='')
    datetime = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0) 
    
    def like(self):
        self.rating += 1
        
    def dislike(self):
        self.rating -= 1  
        
    def __str__(self):
        return f'{self.user.username}: {self.text}'
