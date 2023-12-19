from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    contact = models.IntegerField()
