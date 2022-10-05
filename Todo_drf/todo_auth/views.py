from django.contrib.auth import get_user_model
from django.shortcuts import render

from rest_framework import views as api_views
from rest_framework import generics as api_generic_views, serializers
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

UserModel = get_user_model()


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (UserModel.USERNAME_FIELD, 'password')

    # Fix problem with password in plain text
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate(self, data):
        return super().validate(data)

    # Remove password from response
    def to_representation(self, instance):
        result = super().to_representation(instance)
        result.pop('password')
        return result


class RegisterView(api_generic_views.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = CreateUserSerializer


class LoginView(ObtainAuthToken):
    pass


class TestView(APIView):
    def get(self, request):
        return Response({
            'user': request.user.username,
        })


class LogoutView(api_views.APIView):
    @staticmethod
    def __perform_logout(request):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({
            'message': 'User logged out',
        })

    def get(self, request):
        return self.__perform_logout(request)

    def post(self, request):
        return self.__perform_logout(request)