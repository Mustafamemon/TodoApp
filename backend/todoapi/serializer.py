from rest_framework import serializers
from .models import UserDetail, TodoList, SingleTodoList


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetail
        fields = "__all__"


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SingleTodoList
        fields = "__all__"


class TodoListSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer(many=True,read_only=True) 
    status = serializers.CharField(max_length=15, default="Pending")
    description = serializers.CharField(max_length=250,required=True)
    title = serializers.CharField(max_length=100,required=True)

    class Meta:
        model = TodoList
        fields = "__all__"

class TaskDataValidationSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=15, default="Pending")
    description = serializers.CharField(max_length=250, default="")
    title = serializers.CharField(max_length=100, default="task")

class TaskDataValidationSerializer(serializers.Serializer):
    status = serializers.CharField(max_length=15, default="Pending")
    description = serializers.CharField(max_length=250, default="")
    title = serializers.CharField(max_length=100, default="task")