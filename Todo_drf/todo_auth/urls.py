from django.urls import path

from Todo_drf.todo_auth.views import RegisterView, LoginView

urlpatterns = (
    path('register/', RegisterView.as_view(), name='register user'),
    path('login/', LoginView.as_view(), name='login user'),
)
