from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('users', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),
    path('lists/', views.ListList.as_view(), name='list_list'),
    path('lists/<int:pk>', views.ListDetail.as_view(), name='list_detail'),
]