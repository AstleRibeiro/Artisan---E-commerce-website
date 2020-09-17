from django.db import models
from django.contrib.auth.models import User


class AddToCart(models.Model):
    w_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    i_id = models.CharField(max_length=100000000, default="")
