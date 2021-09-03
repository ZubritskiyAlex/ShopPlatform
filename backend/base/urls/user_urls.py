from django.urls import path
from ..views.user_views import MyTokenObtainPairView, getUsers, getUserProfile, registerUser, \
    deleteUser, \
    update_user_profile, getUserById, updateUser

urlpatterns = [

    path('login/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('profile/',getUserProfile, name="users-profile"),

    path('', getUsers, name="users"),

    path('register/', registerUser, name="register"),

    path('profile/update/',update_user_profile, name="user-profile-update"),

    path('<str:pk>/', getUserById, name="user"),

    path('update/<str:pk>/', updateUser, name="user-profile-update"),

    path('delete/<str:pk>/', deleteUser, name="user-delete"),





]