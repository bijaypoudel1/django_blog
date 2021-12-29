from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','description','image_tag']
    search_fields = ['title']
   
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ['title','category', 'image_tag']
    search_fields = ['title']
    list_filter = ('category',)
    