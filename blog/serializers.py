from rest_framework import serializers

from .models import Category, Post, Tag

class PostSerializer(serializers.ModelSerializer):
    
    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    tag = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name',
        many = True,
    )
    
    owner = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )
    
    created_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    
    class Meta:
        model = Post
        fields = ("id", "title", "owner", "desc", "created_time", "category", "tag", "url")
        extra_kwargs = {
            'url': {'view_name': 'api-post-detail'},
        }

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "owner", "body", "created_time", "category")

# implement Category API
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")
        
# implement Tag API
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")