from .views import RegisterView, UserView, UserList, Userupdate, EmailAPI
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register', RegisterView.as_view()), 
    path('login', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
    path('data', UserView.as_view()), 
    path('list', UserList.as_view()), 
    path('update', Userupdate.as_view()), 
    path('send-email', EmailAPI.as_view()), 
]
