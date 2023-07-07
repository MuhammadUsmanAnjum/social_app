from django.db import models
from users.models import User
# Create your models here.



class Post(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE, related_name="my_posts")
    title = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)

    
    
class PostFiles(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="files")
    file = models.FileField(upload_to="post_files/")
    
    
class Like(models.Model):
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_post_id = models.IntegerField()
    