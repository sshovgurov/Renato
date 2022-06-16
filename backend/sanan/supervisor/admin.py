from django.contrib import admin

from .models import Post, Project, Comment, User


admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Post)
admin.site.register(User)