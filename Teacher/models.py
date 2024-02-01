from django.db import models

class Faculty(models.Model):
    FacultyID = models.IntegerField(primary_key=True)
    Prefix = models.CharField(max_length=10)
    Name = models.CharField(max_length=100)
    Designation = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Qualification = models.CharField(max_length=100)
    ResearchArea = models.CharField(max_length=255)
