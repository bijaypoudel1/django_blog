from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.html import format_html
# Create your models here.

#category model

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)


    def image_tag(self):
        return format_html('<img src = "/media/{}" height = 100px width = 100px/>'.format(self.image))

    def __str__(self):
        return self.title
    

class Post(models.Model):
    p_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    url = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/')

    def image_tag(self):
        return format_html('<img src = "/media/{}" height = 100px width = 100px/>'.format(self.image))

    def __str__(self):
        return self.title
    