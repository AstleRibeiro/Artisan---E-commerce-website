from django.db import models


class ArchitecturalPhoto(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    painting_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField(blank=True, null=True)
    cancelled_price = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=2000)
    small_description = models.TextField(max_length=2000)
    specifications = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class AerialPhoto(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField(blank=True, null=True)
    cancelled_price = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=2000)
    small_description = models.TextField(max_length=2000)
    specifications = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class FashionPhoto(models.Model):
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField(blank=True, null=True)
    cancelled_price = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=2000)
    small_description = models.TextField(max_length=2000)
    specifications = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class FineartPhoto(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField(blank=True, null=True)
    cancelled_price = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=2000)
    small_description = models.TextField(max_length=2000)
    specifications = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class SportsPhoto(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField(blank=True, null=True)
    cancelled_price = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=2000)
    small_description = models.TextField(max_length=2000)
    specifications = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class PortraitPhoto(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField(blank=True, null=True)
    cancelled_price = models.IntegerField(blank=True, null=True)
    description = models.TextField(max_length=2000)
    small_description = models.TextField(max_length=2000)
    specifications = models.TextField(max_length=2000)

    def __str__(self):
        return self.name
