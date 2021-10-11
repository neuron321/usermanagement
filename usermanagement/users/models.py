from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Userprofile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.user.username