from django.contrib import admin
from user import models
# Register your models here.

admin.site.register(models.Posts)
admin.site.register(models.PostsReplies)
admin.site.register(models.PostsViews)
admin.site.register(models.PostsLike)