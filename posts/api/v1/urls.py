from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import PostViewSet

router = DefaultRouter()
router.register("post", PostViewSet)
# router.register("comment", PostCommentViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
