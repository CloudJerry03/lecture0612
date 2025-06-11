from django.db import models

# Create your models here.
class Post(models.Model):
    postname = models.CharField(max_length=50)
    contents = models.TextField()
    
class Article(models.Model):
    subject = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    contents = models.TextField()