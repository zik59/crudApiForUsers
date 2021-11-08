from django.urls import path
from .views import users_list, crud_for_user

urlpatterns = [
    path('api/v1/users/', users_list, name='api_v1_users_list_or_create_user'),
    path('api/v1/users/<int:pk>/', crud_for_user, name='api_v1_users_crud'),
]