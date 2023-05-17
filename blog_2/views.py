from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog_2.models import Post
from blog_2.serializers import PostSerializer


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the blog_2 index.")


@api_view(['GET', 'POST'])
def post_list(request):
    # get all the posts
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return HttpResponse(serializer.data)
    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(serializer.data, safe=201)
        return HttpResponse(serializer.errors, safe=400)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, id):
    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PostSerializer(instance=post)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        post.delete()
        return Response("Deleted successfully")
