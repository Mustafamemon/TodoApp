
from .serializer import TodoListSerializer, UserDetailSerializer
from .models import UserDetail, TodoList

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from django.http import JsonResponse
from django.shortcuts import get_object_or_404


def CustomJsonResponse(status,message="",data={}):
    return JsonResponse({
        "status":status,
        "message":message,
        "data":data
    })

class LoginUserView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,context={'request': request})
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return CustomJsonResponse(status.HTTP_200_OK,"User logged in successfully.",{'token': token.key,'user_id': user.pk,'email': user.email})
        except Exception as e:
            print(e)
            result = e.get_codes().get('non_field_errors')
            if result is not None and result[0] == "authorization":
                return CustomJsonResponse(status.HTTP_401_UNAUTHORIZED,"Invalid username or password.")
            else:
                return CustomJsonResponse(status.HTTP_500_INTERNAL_SERVER_ERROR,"Sometihing went wrong with server.")

class RegisterUserView(APIView):
    def post(self, request, format=None):
        if User.objects.filter(email=request.data.get("email")).exists():
            return CustomJsonResponse(status.HTTP_409_CONFLICT,"User with this email already exist.")
        user = User.objects.create_user(
            email=request.data.get("email"),
            password=request.data.get("password"),
        )
        userDetail = UserDetailSerializer(data={"user": user.id})
        if userDetail.is_valid():
            userDetail.save()
            return CustomJsonResponse(status.HTTP_201_CREATED,"User registered succesfully.")
        return CustomJsonResponse(status.Http500,"Failed to regsitered user.")

class LogoutUserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return CustomJsonResponse(status.HTTP_200_OK,"User logged out successfully.")

class UserTodo(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            queryset = TodoList.objects.filter(user_id=UserDetail.objects.get(user=request.user).pk)
        except TodoList.DoesNotExist:
            return CustomJsonResponse(status.HTTP_404_NOT_FOUND,"This item is not exist in the list.")
        serializer = TodoListSerializer(queryset, many=True)
        return CustomJsonResponse(status.HTTP_200_OK,"success",serializer.data)

    def post(self, request):
        request.data['user_id'] = UserDetail.objects.get(user=request.user).pk
        serializer = TodoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return CustomJsonResponse(status.HTTP_201_CREATED,"Todo item added successfully.",serializer.data)
        else:
            key = list(serializer.errors.keys())[0]
            message = serializer.errors[key][0]
            error_string = key + " , " + message
            return CustomJsonResponse(status.HTTP_400_BAD_REQUEST,message=error_string) 
    
    def put(self,request,todo_id,format=None):
        todo = get_object_or_404(TodoList,todo_id=todo_id)
        user_id = UserDetail.objects.get(user=request.user).pk
        if todo.user_id.id ==  user_id:
            request.data['user_id'] = user_id
            serializer = TodoListSerializer(todo,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return CustomJsonResponse(status.HTTP_200_OK,"Todo item updated successfullly.",serializer.data)
        return CustomJsonResponse(status.HTTP_401_UNAUTHORIZED,"Failed to update todo item.")

    def delete(self,request,todo_id,format=None):
        todo = get_object_or_404(TodoList,todo_id=todo_id)
        if todo.user_id.id ==  UserDetail.objects.get(user=request.user).pk:
            todo.delete()
            return CustomJsonResponse(status.HTTP_200_OK,"Todo item deleted successfully.")
        return CustomJsonResponse(status.HTTP_401_UNAUTHORIZED,"Failed to delete todo item.")