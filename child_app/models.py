from django.db import models
from django.db.models.fields import DecimalField

dir='storage/images'
# Create your models here.
class Parent(models.Model):
    #id=models.BigAutoField(primary_key=True)
    firstName=models.CharField(name='first_name',max_length=50)
    lastName=models.CharField(name='_name',max_length=50)
    birthDate=models.DateField(null=True,blank=True)
    photo=models.ImageField(null=True,blank=True,upload_to=dir)
class Child(models.Model):
    firstName=models.CharField(name='first_name',max_length=50)
    lastName=models.CharField(name='_name',max_length=50)
    birthDate=models.DateField(null=True,blank=True)
    studyLevel=models.PositiveIntegerField(null=True,blank=True)
    photo=models.ImageField(null=True,blank=True,upload_to=dir)
    idParent=models.ForeignKey(Parent,on_delete=models.CASCADE)
class  Place(models.Model):
    longitude=models.DecimalField()
    attitude=models.DecimalField()
    childplaces=models.ManyToManyField(Child)
