from django.db import models

# Create your models here.
class employees(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=200)
    basic=models.IntegerField()
    status=models.IntegerField(default=1)