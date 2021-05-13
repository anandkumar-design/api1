from django.db import models

class emp(models.Model):
    Name = models.CharField(max_length=20,default="", editable=False)
    email = models.CharField(max_length=20,default="", editable=False)