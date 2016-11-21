from __future__ import unicode_literals

from django.db import models

class Employee(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=30)
	address = models.CharField(max_length=60)
	email = models.EmailField()
	phone = models.CharField(max_length=10)
	smartphone = models.BooleanField()

class Customer(models.Model):
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=30)
	address = models.CharField(max_length=60)
	email = models.EmailField()
	phone = models.CharField(max_length=10)


# Create your models here.
