from django.urls import path

from Todo_drf.api import views as views

urlpatterns = (
    path('', views.apioverview, name='api-overview'),
)
