from django.db import models
from category.models import Category
from user.models import CustomUser
from tag.models import Tag
# Create your models here.

class Article (models.Model):
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    title = models.CharField(
        max_length=50
    )
    body = models.TextField()
    tags = models.ManyToManyField(
        Tag
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )