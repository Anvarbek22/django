from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  cmail = models.TextField()
  age = models.TextField()
  phone=models.TextField()
  male=models.TextField()
  password=models.TextField()


# Create your models here.
