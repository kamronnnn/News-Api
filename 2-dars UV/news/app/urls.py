from django.urls import path
from .views import CategoryApiView, NewsApiView, CommentApiView

urlpatterns = [
    path('api/v1/category/', CategoryApiView.as_view()),
    path('api/v1/news/', NewsApiView.as_view()),
    path('api/v1/comments/', CommentApiView.as_view()),
]
