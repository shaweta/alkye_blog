from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Post
from rest_framework.authtoken.models import Token
from django.urls import reverse
class PostModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john', password='12345')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='token ' + self.token.key)
        Post.objects.create(
            title='Test Post',
            content='Just a test post.',
            author=User.objects.get(username='john')
        )

    def test_post_creation(self):
        post = Post.objects.get(title='Test Post')
        self.assertEqual(post.author.username, 'john')
        self.assertEqual(post.content, 'Just a test post.')


from .models import Comment

class CommentModelTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='john', password='12345')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='token ' + self.token.key)
        post = Post.objects.create(
            title='Another Test Post',
            content='Just another test post.',
            author=self.user
        )
        Comment.objects.create(
            post=post,
            author=self.user,
            text='A test comment.'
        )

    def test_comment_creation(self):
        post = Post.objects.get(title='Another Test Post')
        comment = Comment.objects.first()
        self.assertEqual(comment.post, post)
        self.assertEqual(comment.author,self.user)
        self.assertEqual(comment.text, 'A test comment.')

   