from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Passwordresetcodes(models.Model):
    code = models.CharField(max_length=32)
    email= models.CharField(max_length=120)
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)


class Token(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    token= models.CharField(max_length=48)
    def __str__(self): 
        # ***this function showed when the class make an object***
        return "{}'s Token".format(self.user)



class Expense(models.Model):
    text = models.CharField(max_length=255)
    date = models.DateTimeField()
    amount= models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self): 
        # ***this function showed when the class make an object***
        return "{}-{}-{}".format(self.date,self.user,self.amount)

class Income(models.Model):
    text=models.CharField(max_length=255)
    date = models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self): 
        # ***this function showed when the class make an object***
        return "{}-{}-{}".format(self.date,self.user,self.amount)
