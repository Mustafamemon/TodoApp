from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # TODO LIST with auth
    path('register', RegisterUserView.as_view()),
    path('login', LoginUserView.as_view()),
    path('logout', LogoutUserView.as_view()),
    path('todo',UserTodo.as_view()),
    path('todo/<str:todo_id>',UserTodo.as_view())
]