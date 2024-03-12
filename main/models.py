from django.db import models

# Create your models here.
class React(models.Model):
    user = models.CharField(max_length=30)
    userType = models.CharField(max_length=200)