from .views import RegisterView,LoginView, UserList,UserView,LogoutView, Userdelete, Userid, Userupdate
from django.urls import path

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('list', UserList.as_view()),
    path('detail/<str:pk>/', Userid.as_view()),
    path('update/<str:pk>/', Userupdate.as_view()),
    path('delete/<str:pk>/', Userdelete.as_view())    
    
    
]