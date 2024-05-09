from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.
from rest_framework import viewsets,permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

# users=User.objects.all()
# for user in users:
#     Token.objects.get_or_create(user=user)
class PostViewSet(viewsets.ModelViewSet):
    authentication_classes=[TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_pk'])
