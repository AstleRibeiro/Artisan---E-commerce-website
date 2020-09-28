from django.db import models


# Create your models here.
class ContactUs(models.Model):
    name = models.CharField(max_length=2000)
    email = models.CharField(max_length=2000)
    message = models.CharField(max_length=4000, null=True, blank=True)

    def __str__(self):
        return self.name
