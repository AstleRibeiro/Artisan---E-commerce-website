from django.db import models


class AbstractPainting(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=2000)
    price = models.IntegerField(blank=True, null=True)
    cancelled_price = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField(max_length=2000)
    small_description = models.TextField(max_length=2000)
    specifications = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class WildlifePainting(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=2000)
    price = models.IntegerField(blank=True, null=True)
    cancelled_price = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField(max_length=2000)
    small_description = models.TextField(max_length=2000)
    specifications = models.TextField(max_length=2000)

    def __str__(self):
        return self.name


class PastelPainting(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class InkPainting(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Cart(models.Model):
    painting_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=2000)
    price = models.IntegerField(blank=True, null=True)
    cancelled_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

