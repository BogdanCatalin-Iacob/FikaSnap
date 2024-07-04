from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    '''
    Create a user profile
    '''
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_utdxde.jpg'
    )

    class Meta:
        ordering = ['-created_at']

    def __repr__(self) -> str:
        return f"{self.owner}'s profile"
