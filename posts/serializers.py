from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    '''
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    '''
    owner = serializers.ReadOnlyField(source='owner.user')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def validate_image(self, value):
        '''
        Validate uploaded image size to be less
        than 2MB or width / height less than 4096px
        '''
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'content', 'profile_id', 'profile_image', 'is_owner',
            'image', 'image_filter'
        ]
