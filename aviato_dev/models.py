from django.db import models

# Create your models here.
from django.urls import reverse


class User(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    time_create_account = models.DateTimeField(auto_now_add=True)
    avatar = models.ImageField(upload_to="photos/%Y/%m/%d/")
    is_active = models.BooleanField(default=True)

class News(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", null = True)
    time_create = models.DateTimeField(auto_now_add=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null = True)
    is_published = models.BooleanField(default=True)
    slug = models.SlugField(max_length=256, unique=True, db_index=True, verbose_name="URL")
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news', kwargs={'news_slug': self.slug})

    class Meta:
        verbose_name = "Новости"
        ordering = ['-time_create',
                    'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=256, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return  reverse('cat', kwargs={'cat_id':self.pk})