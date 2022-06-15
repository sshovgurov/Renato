from distutils.command.upload import upload
from enum import auto
from django.db import models
from django.contrib.auth.models import AbstractUser



class Project(models.Model):
    title = models.CharField(max_length=32, unique=True)
    description = models.TextField(max_length=255, blank=True, null=True)


class User(AbstractUser):
    SUPERVISOR = 'Supervisor'
    ADMIN = 'Admin'
    MODERATOR = 'Moderator'
    CHOISES = (
        (SUPERVISOR, 'Supervisor'),
        (ADMIN, 'Admin'),
        (MODERATOR, 'Moderator'),
    )
    bio = models.TextField(
        'Биография',
        blank=True,
        null=True
    )
    role = models.CharField(max_length=1, choices=CHOISES, default=SUPERVISOR)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)


class Post(models.Model):
    text = models.TextField(max_length=255)
    score = models.PositiveBigIntegerField
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
        "отчет",
        Post,
        on_delete=models.CASCADE,
        drelated_name='comments'
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
        'Автор комментария',
        User,
        on_delete=models.CASCADE,
        related_name='comments',
    )