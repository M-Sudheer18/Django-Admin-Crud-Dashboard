from django.db import models

# Create your models here.
# Course --> Table Name 
# Table Name == Models 
# models --> Base Model
# Model --> Sub Model 

# For Courses Data to be Save in Database
class Course(models.Model):
    cname  = models.CharField(max_length = 50)
    cdur   = models.IntegerField()
    cprice = models.FloatField()
    
# For Student to be Save in the Database
class student(models.Model):
    name  = models.CharField(max_length = 50)
    email = models.EmailField()