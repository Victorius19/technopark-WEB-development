from django.contrib import admin

# Register your models here.
from app.models import Profile, Question, Tag, Comment, Like

admin.site.register(Profile)
admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)