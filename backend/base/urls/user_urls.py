from django.urls import path
from ..views.user_views import MyTokenObtainPairView, getUsers, getUserProfile, registerUser, \
    deleteUser,\
    update_user_profile


urlpatterns = [

    path('login/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('profile/',getUserProfile, name="users-profile"),

    path('', getUsers, name="users"),

    path('register/', registerUser, name="register"),

    path('profile/update/',update_user_profile, name="user-profile-update"),

    path('delete/<str:pk>/', deleteUser, name="user-profile-update"),



]