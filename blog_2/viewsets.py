from rest_framework import viewsets

from blog_2.models import Post
from blog_2.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer