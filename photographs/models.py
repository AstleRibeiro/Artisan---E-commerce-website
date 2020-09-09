from django.db import models


class ArchitecturalPhoto(models.Model):
    painting_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class AerialPhoto(models.Model):
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class FashionPhoto(models.Model):
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class FineartPhoto(models.Model):
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class SportsPhoto(models.Model):
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class PortraitPhoto(models.Model):
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name
