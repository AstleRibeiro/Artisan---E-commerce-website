# Generated by Django 3.1.1 on 2020-09-28 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(blank=True, max_length=4000, null=True),
        ),
    ]