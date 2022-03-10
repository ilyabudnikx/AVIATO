from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    time_create_account = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d/")


class News(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)