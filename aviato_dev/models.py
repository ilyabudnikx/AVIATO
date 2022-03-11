from django.db import models

# Create your models here.
from django.urls import reverse


class User(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    time_create_account = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d/")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT)

class News(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_id': self.pk})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name