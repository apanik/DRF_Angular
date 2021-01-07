from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework import permissions
from django_iamge.api.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.utils import json

from .models import Post


@api_view(['GET', 'POST'])
def post_collection(request):
    if request.method == 'GET':
        posts = Post.objects.values('title').distinct()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = {'title': request.data.get('title'), 'image': request.FILES.get('image')}
        print(request.data.get('image'))
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            posts = Post.objects.values('title').distinct()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def detail_collection(request,title):
    if request.method == "GET":
        data = Post.objects.filter(title=title)
        serializer = PostSerializer(data, many=True)
        return Response(serializer.data)

