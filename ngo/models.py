from email.policy import default
from django.db import models

# Create your models here.
class ngo_profile(models.Model):
    ngo_name = models.CharField(max_length=30)
    owner_name = models.CharField(max_length=30)
    Contact_no = models.IntegerField()
    area_head = models.CharField(max_length=30,default="null")
    areas = models.CharField(max_length=200,default="null")
    Email = models.EmailField()
    Password = models.CharField(max_length=30)
    authorized = models.BooleanField(default=0)
    #pp_img = models.URLField(default="null")
    
    def __str__(self):
        return (self.ngo_name)

class posts(models.Model):
    event_name = models.CharField(max_length=30)
    sdate = models.DateField()
    edate = models.DateField()
    narea = models.CharField(max_length=30,default="null")
    nslot = models.CharField(max_length=30,default="null")
    vneeded = models.IntegerField()
    info = models.TextField()
    name = models.CharField(max_length=30,default="null")

    def __str__(self):
        return (self.event_name)