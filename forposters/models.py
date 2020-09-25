from django.db import models


class CampaignPosters(models.Model):
    poster_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
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


class CorporatePosters(models.Model):
    poster_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
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


class ShowPosters(models.Model):
    poster_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
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


class PoliticalPosters(models.Model):
    poster_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
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
