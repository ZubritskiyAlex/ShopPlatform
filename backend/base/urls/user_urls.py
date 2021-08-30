from django.urls import path
from ..views import user_views


urlpatterns = [

    path('login/', user_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('profile/', user_views.getUserProfile, name="users-profile"),

    path('', user_views.getUsers, name="users"),

    path('register/', user_views.registerUser, name="register"),

    path('profile/update/', user_views.update_user_profile, name="user-profile-update"),



]