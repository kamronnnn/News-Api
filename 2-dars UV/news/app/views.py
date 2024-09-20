from rest_framework.response import Response
from rest_framework.views import APIView
from .models import News, Category, Comment
from .serializers import NewsSerializer, CategorySerializer, CommentSerializer


# Create your views here.


class CategoryApiView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class NewsApiView(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)



class CommentApiView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

