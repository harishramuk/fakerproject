from django.db import models

# Create your models here.
class Chennaijob(models.Model):
    Date = models.DateField();
    Company = models.CharField (max_length = 100);
    Tittle = models.CharField (max_length = 100);
    Eligibility = models.CharField(max_length = 100);
    Address = models.CharField(max_length=100);
    Email = models.EmailField();
    PhoneNO = models.IntegerField();

class Banglorejob(models.Model):
    Date = models.DateField();
    Company = models.CharField(max_length = 100);
    Tittle = models.CharField (max_length = 100);
    Eligibility = models.CharField(max_length=100);
    Address = models.CharField(max_length=100);
    Email = models.EmailField();
    PhoneNO = models.IntegerField();

class Hydjob(models.Model):
    Date = models.DateField();
    Company = models.CharField (max_length = 100);
    Tittle = models.CharField (max_length = 100);
    Eligibility = models.CharField(max_length=100);
    Address = models.CharField(max_length=100);
    Email = models.EmailField();
    PhoneNO = models.IntegerField();

class Punejob(models.Model):
    Date = models.DateField();
    Company = models.CharField (max_length = 100);
    Tittle = models.CharField (max_length = 100);
    Eligibility = models.CharField(max_length=100);
    Address = models.CharField(max_length=100);
    Email = models.EmailField();
    PhoneNO = models.IntegerField();
