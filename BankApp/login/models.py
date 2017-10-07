from django.db import models


class Customer(models.Model):
    customer_ID = models.CharField(primary_key=True, max_length=12)
    customer_description = models.CharField(max_length=1000)
    accountID = models.ForeignKey(Account.accountID, on_delete=models.CASCADE)


class Name(models.Model):
    customerID = models.ForeignKey(Customer.customer_ID, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    initials = models.CharField(max_length=2)


class Login(models.Model):
    loginID = models.CharField(primary_key=True, max_length=12)
    customerID = models.ForeignKey(Customer.customer_ID, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)


class Account(models.Model):
    accountID = models.CharField(primary_key=True, max_length=12)
    account_BSB = models.ForeignKey(Bank.BSB, on_delete=models.CASCADE)
    account_type = models.CharField(max_length=20)
    account_balance = models.CharField(max_length=100000000)
    account_description = models.CharField(max_length=100)


class Bank(models.Model):
    BSB = models.CharField(max_length=6)
    bank_name = models.CharField(max_length=50)
    bank_mailing_address = models.CharField(max_length=100)


class ContactDetails(models.Model):
    contactID = models.CharField(primary_key=True,max_length=12)
    customer_ID = models.ForeignKey(Customer.customer_ID, on_delete=models.CASCADE)
    email_address = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=12)


class Address(models.Model):
    contactID = models.ForeignKey(ContactDetails.contactID, on_delete=models.CASCADE)
    street_number = models.CharField(max_length=5)
    street_name = models.CharField(max_length=50)
    suburb = models.CharField(max_length=50)
    postcode = models.CharField(max_length=4)
    state = models.CharField(max_length=18)
    country = models.CharField(max_length=50)


class Transfer(models.Model):
    transferID = models.CharField(primary_key=True, max_length=12)
    accountID = models.ForeignKey(Account.accountID, on_delete=models.CASCADE)
    amount = models.CharField(max_length=10)
    transfer_description = models.CharField(max_length=140)
