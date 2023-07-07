from django.contrib import admin
from .models import PostFiles, Post, Like
# Register your models here.

class PostFilesInlineAdmin(admin.StackedInline):
    model = PostFiles
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostFilesInlineAdmin]
    list_display = ['id', 'title', 'owner']

    class Meta:
        model = Post
        
        
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'liked_by', 'liked_post_id']
