from django.db import models

# Create your models here.

class Tag(models.Model):
    body = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.body