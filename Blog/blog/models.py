from django.db import models
from django.contrib.auth.models import User

class BLOG(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100, null=True, blank=True)
    img = models.ImageField(upload_to='images/') 
    content=models.TextField()
    created_by = models.ForeignKey(User, related_name='blog_user',on_delete = models.CASCADE)
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    is_activeis_active = models.BooleanField(default=True)

    class Meta:
        db_table = "blogs"

class LIKE(models.Model):
    blog=models.ForeignKey(BLOG,related_name='blog',on_delete = models.CASCADE)
    created_by = models.ForeignKey(User, related_name='like_user',on_delete = models.CASCADE)
    create_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created at')
    
    class Meta: 
        db_table = "likes"
        