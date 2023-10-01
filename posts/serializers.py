from rest_framework import serializers

from users.serializers import ProfileSerializer
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("pk","profile", "post", "text")

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("post", "text")

class PostSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True) # nested serialzer : 시리얼라이저 내에 들어가는 또 다른 시리얼라이저
    # 하위 JSON 객체를 만들 때 사용
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ("pk", "profile", "title", "body", "image", "published_date", "likes", "comments")
    
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "category", "body", "image")