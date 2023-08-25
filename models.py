
from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=15)
    econtact=models.CharField(max_length=15)
    class meta:
        db_table="Employee"