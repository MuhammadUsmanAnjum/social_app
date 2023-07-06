from .serializers import PostCreateSerializer, PostSerializer, PostFilesSerializer
from posts.models import Post, PostFiles
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class PostViewSet(ModelViewSet):
    http_method_names = ["get", "post", "delete"]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()

    
    def get_queryset(self):
        return Post.objects.all()
    def get_serializer_class(self):
        serializer_class = PostSerializer
        if self.action == "create":
            serializer_class = PostCreateSerializer

        return serializer_class


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        created_obj = serializer.create(serializer.validated_data)
        response_serializer = PostSerializer(created_obj, context={'request': request})
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)

