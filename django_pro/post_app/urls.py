from django.urls import path
from .views import PostAPI, PostDetailsAPI

urlpatterns = [
    path('posts/', PostAPI.as_view()),
    path('posts/<int:pk>/', PostDetailsAPI.as_view())
]