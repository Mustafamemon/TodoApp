from rest_framework import serializers
from .models import UserDetail, TodoList


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = "__all__"

class TodoListSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(many=True,read_only=True) 
    status = serializers.CharField(max_length=15, default="Pending")
    description = serializers.CharField(max_length=250,required=True)
    title = serializers.CharField(max_length=100,required=True)

    class Meta:
        model = TodoList
        fields = "__all__"
