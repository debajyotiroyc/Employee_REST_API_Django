from django.db import models

# Create your models here.
class employee(models.Model):
    f_name=models.CharField(max_length=15)
    l_name = models.CharField(max_length=15)
    emp_id=models.IntegerField()

    def __str__(self):
        return self.f_name

