from django.db import models


# Create your models here.
class Madhubani(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=2000)
    image = models.ImageField()
    price = models.IntegerField(blank=True, null=True)
    small_description = models.TextField(max_length=2000)
    specifications = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
