from .serializers import PostCreateSerializer, PostSerializer, PostFilesSerializer, LikeSerializer
from posts.models import Post, PostFiles, Like
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from users.models import User
from users.api.v1.serializers import UserSerializer


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


    @action(detail=True, methods=['post'])
    def like(self, request, *args, **kwargs):
        data = request.data 
        serializer = LikeSerializer(data=data)
        if serializer.is_valid():
            if not Like.objects.filter(liked_by=data['liked_by'], liked_post_id=data['liked_post_id']):
                serializer.save()
                user = User.objects.get(id=data['liked_by'])
                user_serializer = UserSerializer(user)
                res = {'like_detail': serializer.data, 'user_detail':user_serializer.data}
                return Response(res,  status=status.HTTP_201_CREATED)
            else:
                return Response({'message':"Post Already Liked!"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
    @action(detail=True, methods=['post'])
    def unlike(self, request, *args, **kwargs):
        data = request.data 
        try:
            query = Like.objects.get(liked_by=data['liked_by'], liked_post_id=data['liked_post_id'])
            if query:
                query.delete()
                return Response({"message":"Post Unliked!"}, status=status.HTTP_200_OK)
        except:
             return Response({"message":"Post Unliked!"}, status=status.HTTP_200_OK)
            
        