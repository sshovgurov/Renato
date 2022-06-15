from django.contrib.auth.models import AbstractUser
from django.db import models
#from supervisor.models import Project


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
    #project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True)