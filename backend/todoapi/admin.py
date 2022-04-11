from django.contrib import admin
from .models import  TodoList ,UserDetail,User
# Register your models here.
admin.site.register(TodoList)
admin.site.register(UserDetail)
admin.site.register(User)