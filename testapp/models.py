from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    empcode = models.CharField(max_length=50)
    empdept = models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=50,null=True)
    gender = models.CharField(max_length=50,null=True)
    joiningdate = models.DateField(null=True)

    def __str__ (self):
        return self.user.username

class EmployeeEducation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    coursepg = models.CharField(max_length=100,null=True)
    schoolclgpg = models.CharField(max_length=100,null=True)
    yearofpassingpg = models.CharField(max_length=20,null=True)
    percentagepg= models.CharField(max_length=30,null=True)
    courseug = models.CharField(max_length=100,null=True)
    schoolclgug = models.CharField(max_length=100,null=True)
    yearofpassingug = models.CharField(max_length=20,null=True)
    percentageug= models.CharField(max_length=30,null=True)
    coursessc = models.CharField(max_length=100,null=True)
    schoolclgssc = models.CharField(max_length=100,null=True)
    yearofpassingssc = models.CharField(max_length=20,null=True)
    percentagessc= models.CharField(max_length=30,null=True)
    coursehsc = models.CharField(max_length=100,null=True)
    schoolclghsc = models.CharField(max_length=100,null=True)
    yearofpassinghsc = models.CharField(max_length=20,null=True)
    percentagehsc= models.CharField(max_length=30,null=True)


    def __str__ (self):
        return self.user.username


class EmployeeExperince(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    company1name = models.CharField(max_length=100,null=True)
    company1desig = models.CharField(max_length=100,null=True)
    company1sal = models.CharField(max_length=20,null=True)
    company1duration= models.CharField(max_length=100,null=True)
    company2name = models.CharField(max_length=100,null=True)
    company2desig = models.CharField(max_length=100,null=True)
    company2sal = models.CharField(max_length=20,null=True)
    company2duration = models.CharField(max_length=100,null=True)
    company3duration= models.CharField(max_length=30,null=True)
    company3name = models.CharField(max_length=100,null=True)
    company3desig = models.CharField(max_length=100,null=True)
    company3sal = models.CharField(max_length=20,null=True)
    company3duration= models.CharField(max_length=30,null=True)


    def __str__ (self):
        return self.user.username
