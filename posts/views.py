from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
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
    queryset = Post.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get(self, request):
        '''
        Lists all posts
        '''
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        '''
        Create a new post with user's input
        '''
        serializer = PostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetails(APIView):
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def get_object(self, pk):
        '''
        Check if an object exists,
        Handle DoesNotExist error otherwise
        '''
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        '''
        Get a post by id
        '''
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        '''
        Update a post by id
        '''
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        '''
        Delete a post by id
        '''
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
