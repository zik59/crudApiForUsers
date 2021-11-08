from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('api-token-auth/', TokenObtainPairView.as_view(), name='api-token-auth_create'),
    path('api-token-auth/refresh/', TokenRefreshView.as_view(), name='api-token-auth_refresh'),
]
