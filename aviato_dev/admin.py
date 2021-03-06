from django.contrib import admin
from .models import *
# Register your models here.

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','photo', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(User)
admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)