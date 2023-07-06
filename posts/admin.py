from django.contrib import admin
from .models import PostFiles, Post
# Register your models here.

class PostFilesInlineAdmin(admin.StackedInline):
    model = PostFiles
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostFilesInlineAdmin]

    class Meta:
        model = Post