from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    Created_At = models.DateTimeField(auto_now_add = True)
    