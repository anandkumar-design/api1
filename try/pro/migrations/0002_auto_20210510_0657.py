# Generated by Django 3.2 on 2021-05-10 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp',
            name='Name',
            field=models.CharField(default='', editable=False, max_length=20),
        ),
        migrations.AddField(
            model_name='emp',
            name='email',
            field=models.CharField(default='', editable=False, max_length=20),
        ),
    ]
