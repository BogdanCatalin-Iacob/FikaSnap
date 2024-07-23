from rest_framework import serializers
from .models import Like


class LieSerializer(serializers.ModelSerializer):
    '''
    Serializer for Like model
    '''
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields =[
            'id', 'created_at', 'owner',' post'
        ]
