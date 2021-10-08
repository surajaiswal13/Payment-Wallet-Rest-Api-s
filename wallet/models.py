from django.db import models
from django.contrib.auth import get_user_model
# from accounts.models import User
User = get_user_model()

# Create your models here.

class Wallet(models.Model):
    user = models.ForeignKey(User,related_name='blog',on_delete=models.CASCADE,null=False)
    balance = models.IntegerField(default=0)