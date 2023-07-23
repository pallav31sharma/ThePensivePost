from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
# Create your models here.
from ckeditor.fields import RichTextField
#Category Model
from tinymce.models import HTMLField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    add_date = models.DateTimeField(auto_now_add=True, null=True)

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="width:40px;height:40px;border-radius:50%;"  />'.format(self.image))

    def __str__(self):
        return self.title


# Post Mode
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    content = RichTextUploadingField()
    url = models.CharField(max_length=100)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


# Test Mode
# class Test(models.Model):
#     post_id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=200)
#     content = RichTextUploadingField()
#     url = models.CharField(max_length=100)
#     cat = models.ForeignKey(Category, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='post/')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.title

