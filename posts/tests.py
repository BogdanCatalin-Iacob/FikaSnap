from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='bogdan', password='pass')

    def test_can_list_posts(self):
        bogdan = User.objects.get(username='bogdan')
        Post.objects.create(owner=bogdan, title='title test')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
