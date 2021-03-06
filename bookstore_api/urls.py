from django.urls import path
from bookstore_api import views
from bookstore_api import users

urlpatterns = [
    path('book/', views.BookAPIView.as_view()),
    path('detail/<int:id>/', views.BookDetails.as_view()),
    path('generic/book/<int:id>/', views.GenericAPIView.as_view()),
    path('users/', users.UsersAPIView.as_view()),
    path('userdetail/<int:id>/', users.userDetails.as_view()),
    path('usercart/<int:id>/', users.userCart.as_view(), name="usercart"), #new class for user cart API
    path('latercart/<int:id>/', users.userSaveLater.as_view(), name="savelater"),#in progress
    path('userwish/<int:id>/', users.userWish.as_view(), name="userwish"),
    path('userwish2/<int:id>/', users.userWish2.as_view(), name="userwish2"),
    path('userwish3/<int:id>/', users.userWish3.as_view(), name="userwish3"),

]
