from django.urls import path
from .views import (
    UserListCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    LoginAPIView,
)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path("login/", LoginAPIView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/users/", UserListCreateView.as_view(), name="user-create"),
    path("api/users/detail/<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("api/users/update/<int:pk>/", UserUpdateView.as_view(), name="user-update"),
    path("api/users/delete/<int:pk>/", UserDeleteView.as_view(), name="user-delete"),
]
