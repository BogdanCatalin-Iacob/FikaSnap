from rest_framework import generics, permissions
from fikasnap_api.permissions import IsOwnerOrReadOnly
from .models import Like
from .serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
    """
    List all likes
    Create a like, i.e. like a user's post.
    Perform_create: associate the current logged in user with a like.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class LikeDetails(generics.RetrieveDestroyAPIView):
    '''
    Retrieve a like or delete it by id if you own it
    '''
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
