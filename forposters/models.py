from django.db import models


class CampaignPosters(models.Model):
    painting_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class CorporatePosters(models.Model):
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class ShowPosters(models.Model):
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name


class PoliticalPosters(models.Model):
    name = models.CharField(max_length=2000)
    integer = models.IntegerField(blank=True, null=True)
    artist = models.CharField(max_length=100)
    image = models.ImageField()

    def __str__(self):
        return self.name
