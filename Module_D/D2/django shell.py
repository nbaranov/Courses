# python3 manage.py shell

# 1 Создать двух пользователей (с помощью метода User.objects.create_user).
from django.contrib.auth.models import User

user1 = User.objects.create_user(username='BillGates', password='MSLoveLinux', email='Bill@microsoft.com')
user1.save()
user2 = User.objects.create_user(username='Mark', password='GiveMeYourData', email='Mark@facebook.com')
user2.save()

# 2 Создать два объекта модели Author, связанные с пользователями.

from accounts.models import Author

author1 = Author.objects.create(user = user1, rating = 0)
author1.save()
author2 = Author.objects.create(user = user2, rating = 0)
author2.save()

# 3 Добавить 4 категории в модель Category.

from news.models import Category

category1 = Category.objects.create(name = 'Интернет')
category2 = Category.objects.create(name = 'Наука')
category3 = Category.objects.create(name = 'Спорт')
category4 = Category.objects.create(name = 'Общество')

# 4 Добавить 2 статьи и 1 новость.

import datetime
from news.models import Post

post1 = Post.objects.create(author=author1, type=Post.post, create_time = datetime.datetime.now(), header='Microsoft created linux destributive', text='когда-нибудь здесь будет много текста, но я пока только учусь. И мне нужно будет проверить как работает метод отрезающий превьюшку', rating=0.0)

post2 = Post.objects.create(author=author1, type=Post.post, create_time = datetime.datetime.now(), header='Билл Гейтс не будет чипировать людей', text='Основатель компании Микрософт заявил, что жидких супер-нано-биочипов ему  и самому мало, чтобы тратить их на каких-то там россиян, поэтому можно расслабиться и идти на работу самому, управлять нами не будут.', rating=0.0)

news1 = Post.objects.create(author=author2, type=Post.news, create_time = datetime.datetime.now(), header='Марк Цукурберг заявил, что он  не рептилоид', text='Ну заявил и заявил, чего бухтеть то. Тоже мне новость.', rating=0.0)

# 5 Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
post1.category.add(category1)
post1.save()
post2.category.add(category1, category2, category4)
post2.save()
news1.category.add(category1, category4)
news1.save()

# 6 Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
from news.models import Comment

comment1 = Comment.objects.create(post=post1, user=user1, datetime=datetime.datetime.now(), rating=0.0, text='Microsoft love Linux')
comment2 = Comment.objects.create(post=post2, user=user1, datetime=datetime.datetime.now(), rating=0.0, text='Еще не всех рептилоидов чипировали')
comment3 = Comment.objects.create(post=post2, user=user2, datetime=datetime.datetime.now(), rating=0.0, text='Я не рептилоид')
comment4 = Comment.objects.create(post=news1, user=user2, datetime=datetime.datetime.now(), rating=0.0, text='Но ведь...')
comment5 = Comment.objects.create(post=post1, user=user2, datetime=datetime.datetime.now(), rating=0.0, text='Ха-ха!')


# 7 Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
post1.like()
post1.like()
post1.like()
post1.save()

post2.like()
post2.like()
post2.save()

news1.dislike()
news1.dislike()
news1.dislike()
news1.dislike()
news1.save()

comment1.dislike()
comment1.save()

comment2.like()
comment2.like()
comment2.save()

comment4.like()
comment4.like()
comment4.like()
comment4.like()
comment4.like()
comment4.like()
comment4.save()

comment5.like()
comment5.like()
comment5.like()
comment5.like()
comment5.save()

# 8 Обновить рейтинги пользователей.

author1.update_rating()
author2.update_rating()

# 9 Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
# некрасиво
Author.objects.all().order_by('-rating').values('user__username', 'rating')[0]

# красивее
best_user = Author.objects.all().order_by('-rating').values('user__username', 'rating')[0]
print(f"Лучший пользователь: {best_user['user__username']}, рейтинг: {best_user['rating']}")

# 10 Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
# некрасиво без превью
Post.objects.all().order_by('-rating').values('create_time', 'author__user__username', 'rating', 'header')[0]

# красивее с превью
best_post = Post.objects.all().order_by('-rating')[0]

print(f"Лучшая статья: {best_post.header}\n{best_post.preview()}\n\n\
Автор: {best_post.author.user.username}\n\
Рейтинг: {best_post.rating}\n\
Дата публикации: {str(best_post.create_time).split('.')[0]}")


# 11 Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
# некрасиво
Comment.objects.filter(post=Post.objects.all().order_by('-rating')[0]).order_by('-rating').values('datetime', 'user__username', 'rating', 'text')

#красивее
best_post_comments = Comment.objects.filter(post=Post.objects.all().order_by('-rating')[0]).order_by('-rating')

for comment in best_post_comments:
    print(f"{str(comment.datetime).split('.')[0]} {comment.user.username} {comment.rating} {comment.text}")
