from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count
from rest_framework import generics, permissions, filters
from fikasnap_api.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    '''
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    '''
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at'
    ]

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class PostDetails(generics.RetrieveUpdateDestroyAPIView):
    '''
    Retrieve a post and edit or delete it if you own it.
    '''
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.all()
