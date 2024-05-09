from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/<int:post_pk>/comments/', views.CommentViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='post-comments'),
     path("posts/<int:post_pk>/comments/<int:pk>/",
        views.CommentViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }),
        name="comment_detail",
    ),
]
