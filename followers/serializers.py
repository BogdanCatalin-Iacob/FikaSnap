from rest_framework import serializers
from django.db import IntegrityError
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    Create method handles the unique constraint on 'owner' and 'followed'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'created_at', 'followed', 'followed_name'
        ]

    def create(self, validated_data):
        '''
        Handle dupliocated follower
        '''
        try:
            return super().create(validated_data)
        except IntegrityError:
            serializers.ValidationError(
                {'detail': 'possible duplicate'}
            )
