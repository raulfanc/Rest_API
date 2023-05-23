from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from blog_2.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body']

    # title = serializers.CharField(max_length=255)
    # body = serializers.CharField()
    #
    # def create(self, validated_data):
    #     """this function is to create a new post, and validate the data"""
    #     return Post.objects.create(validated_data)
    #
    # def update(self, instance, validated_data):
    #     """this function is to update a post, instance is the post that we want to update, and validated_data is the data that we want to update"""
    #     """save the data to the database, and return the instance"""
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.body = validated_data.get('body', instance.body)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'token']
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        }}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        token = Token.objects.create(user=user)
        print(token)
        return user

    # get the token
    def get_token(self, user):
        try:
            token = Token.objects.get(user=user)
            return token.__dict__['key']
        except Token.DoesNotExist:
            token = Token.objects.create(user=user)
            return token.__dict__['key']

