from django.db import models


# Create your models here.

#
class Auction(models.Model):
    username = models.CharField(max_length=2000)
    bid = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.username
