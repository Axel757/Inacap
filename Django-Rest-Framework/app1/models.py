from typing import Any
from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.id) + " " + str(self.name) + "($" + str(self.salary) + ")"
    
    class Meta:
        ordering = ['-id']
        
class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=5, decimal_places=2)   
    
    def __str__(self):
        return str(self.id) + " " + str(self.name) + "(SCORE: " + str(self.score)+ ")"
        
    