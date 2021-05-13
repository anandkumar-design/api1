from django.db import models

class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    score = models.DecimalField(max_digits=19,decimal_places=10)

    def __self__(str):
        return self.id+self.name+self.score

