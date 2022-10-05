from django.db import models

# Create your models here.

class AdmissionModel(models.Model):
    Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    City = models.CharField(max_length=100)
    Roll_No = models.IntegerField()
    Address = models.CharField(max_length=100)
    Fees = models.IntegerField()

    def __str__(self):
        return self.Name
