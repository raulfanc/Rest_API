from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView

from blog_2.models import Post
from blog_2.permissions import IsAuthorOrReadOnly
from blog_2.serializers import PostSerializer, UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request):
#         print("this is the request", request)
#         return self.list(request)
#
#     def create(self, request):
#         self.create(request)


# class PostDetail(GenericAPIView, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = 'id'
#
#     def get(self, request, id):
#         return self.retrieve(request, id=id)
#
#     def put(self, request, id):
#         return self.update(request, id=id)
#
#     def delete(self, request, id):
#         return self.destroy(request, id=id)
