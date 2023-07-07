from posts.models import Post, PostFiles, Like
from rest_framework import serializers
from users.api.v1.serializers import UserSerializer


class PostFilesSerializer(serializers.ModelSerializer):

    class Meta:
        model = PostFiles
        fields = ["id", "file"]
        
        
class PostSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    files = PostFilesSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ["id", "title", "description", "owner", "files"] 
        
        
class PostCreateSerializer(serializers.ModelSerializer):
    files = serializers.ListField(child=serializers.FileField(max_length=100000))
    class Meta:
        model = Post
        fields = ["title", "description", "files"]


    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        files = validated_data.pop("files")
        post = Post.objects.create(owner=user, **validated_data)
        post_files = []
        for file in files:
            post_files.append(PostFiles(post=post, file=file))
        PostFiles.objects.bulk_create(post_files)
        return post
    
    
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'