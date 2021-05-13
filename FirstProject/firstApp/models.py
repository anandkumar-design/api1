from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    sal = models.DecimalField(max_digits=19,decimal_places=10)

    def __self__(str):
        return self.id+self.name+self.sal