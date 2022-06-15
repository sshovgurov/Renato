from distutils.command.upload import upload
from enum import auto
from django.db import models
from users.models import User


class Project(models.Model):
    title = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=255, blank=True, null=True)



class Post(models.Model):
    text = models.TextField(max_length=255)
    score = models.PositiveIntegerField
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True, db_index=True)
    author = models.ForeignKey(
        User,
        verbose_name='автор',
        related_name='posts',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.text[:15]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    text = models.TextField(
        'Текст комментария',
        max_length=255
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True,
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )