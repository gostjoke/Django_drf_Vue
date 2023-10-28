from django.shortcuts import render
from rest_framework import serializers

from rest_framework.views import APIView
from viewApp.models import Author, Book, Publish
from rest_framework.response import Response

# Create your views here.
# 原生不知道數據往哪張表添加
class AuthorSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=32)
    age = serializers.IntegerField()

    ## must rewrite the hook because original create was catch error
    def create(self, validated_data): 
        author_obj = Author.objects.create(**validated_data)

        return author_obj

    def update(self, instance, validated_data):
        Author.objects.filter(pk=instance.pk).update(**validated_data)
        return instance

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
        
class AuthorDetailView(APIView): #可用來捕獲主鍵
    def get(self, request, id):
        author = Author.objects.get(pk=id)
        serializer = AuthorSerializers(instance=author,many=False)

        return Response(serializer.data)

    def put(self, request, id):
        author = Author.objects.get(pk=id)
        serializer = AuthorSerializers(instance=author,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("OK")
        else:
            return Response(serializer.errors)
        
    def delete(self, request, id):
        Author.objects.get(pk=id).delete()
        return Response("delete ok")
    
#################################################################################################

# class PublishSerializers(serializers.ModelSerializer):

#     ### the samething as serializer 
#     class Meta:
#         model = Publish
#         fields = "__all__"

# class PublishView(APIView):

#     def get(self, request):
#         publish_list = Publish.objects.all()
#         # instance 是 get
#         serializer = PublishSerializers(instance=publish_list, many=True) # many default False means one object

#         return Response(serializer.data)

#     def post(self, request):
#         serializer = PublishSerializers(data = request.data)
#         # 數據較正: 通過驗證serializer.validate_data, 未通過serializer.errors
#         if serializer.is_valid(): # 所有的字段通過驗證
#             # Publish_obj = Publish.objects.create(**serializer.validate_data)
#             serializer.save()
#             return Response("OK")
#         else:
#             return Response(serializer.errors)
        
# class PublishDetailView(APIView): #可用來捕獲主鍵
#     def get(self, request, id):
#         Publisher = Publish.objects.get(pk=id)
#         serializer = PublishSerializers(instance=Publisher,many=False)

#         return Response(serializer.data)

#     def put(self, request, id):
#         Publisher = Publish.objects.get(pk=id)
#         serializer = PublishSerializers(instance=Publisher,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response("OK")
#         else:
#             return Response(serializer.errors)
        
#     def delete(self, request, id):
#         Publish.objects.get(pk=id).delete()
#         return Response("delete ok")

#### publish 新寫法
from rest_framework.generics import GenericAPIView
## GenericAPIView 核心是做封裝
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class PublishSerializers(serializers.ModelSerializer):

    ### the samething as serializer 
    class Meta:
        model = Publish
        fields = "__all__"
"""
class PublishView(GenericAPIView, ListModelMixin, CreateModelMixin ):

    queryset = Publish.objects
    serializer_class = PublishSerializers

    ############################################### 
    # 原始寫法 GenericAPIView
    # def get(self, request):
    #     serializer = self.get_serializer(instance=self.queryset, many=True)
    #     return Response(serializer.data)

    # def post(self, request):   
    #     serializer = self.get_serializer(data=request.data)
    #     if serializer.is_valid(): # 所有的字段通過驗證
    #         # Publish_obj = Publish.objects.create(**serializer.validate_data)
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors)
    ###############################################
    
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class PublishDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin): #可用來捕獲主鍵

    queryset = Publish.objects
    serializer_class = PublishSerializers

    ############################################### 
    # 原始寫法 GenericAPIView
    ## pk 寫法
    # def get(self, request, pk):

    #     serializer = self.get_serializer(instance=self.get_object(), many=False)

    #     return Response(serializer.data)

    # def put(self, request, pk):

    #     serializer = self.get_serializer(instance=self.get_object(),data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response("OK")
    #     else:
    #         return Response(serializer.errors)
        
    # def delete(self, request, id):
    #     Publish.objects.get(pk=id).delete()
    #     return Response("delete ok")
    ############################################### 
    def get(self, request, pk):
        return self.retrieve(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request,pk)
"""
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# class PublishView(ListCreateAPIView):

#     queryset = Publish.objects
#     serializer_class = PublishSerializers
    

# class PublishDetailView(RetrieveUpdateDestroyAPIView): 

#     queryset = Publish.objects
#     serializer_class = PublishSerializers

from rest_framework.viewsets import ViewSetMixin

# 是一套路由機制的改變
# class PublishView(ViewSetMixin, APIView):

#     def list(self, request):
#         return Response("List...")
    
#     def create(self, request):
#         return Response("create...")
#     def single(self, request):
#         return Response("single...")
#     def edit(self, request):
#         return Response("edit...")
# class PublishView(ViewSetMixin, GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin, CreateModelMixin):

#     queryset = Publish.objects
#     serializer_class = PublishSerializers

## the easiest way to write
from rest_framework.viewsets import ModelViewSet

class PublishView(ModelViewSet):
    
    queryset = Publish.objects
    serializer_class = PublishSerializers



