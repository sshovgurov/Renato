from django.contrib import admin

from .models import Post, Project, Comment


admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Post)
