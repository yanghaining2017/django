from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname=models.CharField(max_length=20)
    upwd=models.CharField(max_length=40)
    umail=models.CharField(max_length=30)
    ushou=models.CharField(max_length=50)
    uaddress=models.CharField(max_length=100)
    ucode=models.CharField(max_length=6)
    uphone=models.CharField(max_length=11)