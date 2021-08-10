from django.db import models
from django.contrib.auth.models import User
from accounts.models import Author



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
    header = models.CharField(max_length=124, 
                              default='Заголовок отсутвует')
    text = models.TextField(default='Текст отсутствует')
    rating = models.FloatField(default=0.0)
    
    def like(self):
        self.rating += 1
        
    def dislike(self):
        self.rating -= 1   
    
    def preview(self):
        return f'{self.text[:124]} ...'
    
    # def __repr__(self):
    #     return f'{self.preview} \n {self.create_time} \t {self.author}'

class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


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
