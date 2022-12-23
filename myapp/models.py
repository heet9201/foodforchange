from django.db import models


class profile(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=30,default="null")
    Address = models.CharField(max_length=30,default="null")
    Contact_no = models.IntegerField()
    Email = models.EmailField()
    Password = models.CharField(max_length=30)
    pp_img = models.URLField(default="null")
    
    def __str__(self):
        return ((self.First_name)+"_"+(self.Last_name))

class vsession(models.Model):
    vdate = models.DateField()
    vslot = models.CharField(max_length=30,default="null")
    vevent = models.CharField(max_length=30,default="null")
    Email = models.EmailField(default="null")

    def __str__(self):
        return (self.vevent)

