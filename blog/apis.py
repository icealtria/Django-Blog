from rest_framework import generics, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Post, Category, Tag
from .serializers import PostSerializer, CategorySerializer, TagSerializer, PostDetailSerializer

# @api_view(['GET'])
# def post_list(request):
#     posts = Post.objects.all()
#     serializer = PostSerializer(posts, many=True)
#     return Response(serializer.data)

# class PostList(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
# @api_view(['GET'])
# def post_detail(request, pk):
#     post = Post.objects.get(pk=pk)
#     serializer = PostSerializer(post)
#     return Response(serializer.data)

# class PostDetail(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.filter(status=Post.STATUS_PUBLISHED)
    serializer_class = PostSerializer
    # 限制方法 GET
    http_method_names = ['get']
    
    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ['get']
    
    # retrieve
    def retrieve(self, request, pk):
        posts = Post.objects.filter(category_id=pk)
        serializer = PostDetailSerializer(posts, many=True)
        return Response(serializer.data)
    
    