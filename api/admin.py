from django.contrib import admin
from .models import Task, Post

# AdminページでTaskとPostを管理できるように設定
admin.site.register(Post)
admin.site.register(Task)
