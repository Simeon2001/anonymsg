from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post (models.Model):
    
    text = models.TextField(max_length=1000)
    name = models.ForeignKey(User,on_delete=models.CASCADE,related_name='ano_name')
    nickname = models.CharField(max_length=14)
    date_created= models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.text
    
    def get_absolute_url(self):
        return reverse ('post_detail/',args=[self.nickname])
    
    
class Comment (models.Model):
    
    post = models.ForeignKey(Post, null=True,on_delete=models.CASCADE,related_name='comments')
    
    text = models.TextField(max_length=1000)
    
    date_created= models.DateTimeField(auto_now_add=True,null=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.text