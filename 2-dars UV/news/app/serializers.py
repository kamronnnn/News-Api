from rest_framework import serializers
from .models import Comment, Category, News


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------
# --------------------------------------------------


# Bu dars da yozilganlar

# import io
# from rest_framework.parsers import JSONParser
# from rest_framework.renderers import JSONRenderer
#
# class News:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content
#
#
# news = News("Bu yerda nima", "Bu yerda nimadir boldi")
#
#
# class NewsSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=150)
#     content = serializers.CharField()
#
# def convert_to_json():
#     serializer = NewsSerializer(news)
#     print(serializer.data)
#
#     json = JSONRenderer().render(serializer.data)
#     print(json)
#
# def json_to_python():
#     json = b'{"title":"Bu yerda nima", "content":"Bu yerda nimadir boldi"}'
#     stream = io.BytesIO(json)
#     data = JSONParser().parse(stream)
#     serializer = NewsSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
