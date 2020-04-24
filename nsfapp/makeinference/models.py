from django.db import models

class Post(models.Model):
    message = models.TextField(max_length=10000)
