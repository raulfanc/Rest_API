from rest_framework import serializers

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
