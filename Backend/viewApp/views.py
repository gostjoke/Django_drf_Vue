from django.shortcuts import render
from rest_framework import serializers

from rest_framework.views import APIView
from viewApp.models import Author, Book, Publish
from rest_framework.response import Response

# Create your views here.
class AuthorSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    age = serializers.IntegerField()

    ## must rewrite the hook because original create was catch error
    def create(self, validated_data): 
        author_obj = Author.objects.create(**validated_data)

        return author_obj


class AuthorView(APIView):

    def get(self, request):
        authors = Author.objects.all()
        # instance 是 get
        serializer = AuthorSerializers(instance=authors, many=True) # many default False means one object

        return Response(serializer.data)

    def post(self, request):
        serializer = AuthorSerializers(data = request.data)
        # 數據較正: 通過驗證serializer.validate_data, 未通過serializer.errors
        if serializer.is_valid(): # 所有的字段通過驗證
            # author_obj = Author.objects.create(**serializer.validate_data)
            serializer.save()
            return Response("OK")
        else:
            return Response(serializer.errors)