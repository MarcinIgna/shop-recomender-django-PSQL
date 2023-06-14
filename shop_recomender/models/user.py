from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    registration_date = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)