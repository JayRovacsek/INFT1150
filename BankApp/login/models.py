from django.db import models

class Account(models.Model):
	accountID = models.CharField(primary_key=True, max_length=12)
	password = models.CharField(max_length=20),
	balance = models.CharField(max_length=20)