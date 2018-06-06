from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100, default='')
    age = models.IntegerField(default='')
    phone = models.IntegerField(default='')
    emailid = models.CharField(max_length=100, default='')

def __str__(self):
    return self.name


class Address(models.Model):
    person = models.ForeignKey(Person)
    address = models.CharField(max_length=150)

def __str__(self):
        return (self.address)