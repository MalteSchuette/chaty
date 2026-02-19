from django.db import models

# Create your models here.

class Chat(models.Model):
    name = models.CharField(max_length=30)
    message = models.CharField(max_length=500)
    created_at = models.DateField(auto_now=False,auto_now_add=True)

