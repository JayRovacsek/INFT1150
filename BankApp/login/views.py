from django.shortcuts import render_to_response

from login.models import Customer
from login.models import Name
from login.models import Login
from login.models import Account
from login.models import Bank
from login.models import ContactDetails
from login.models import Address
from login.models import Transfer

def login(request):
    	return render_to_response('login/index.html')	#Relative templates location added to avoid confusion