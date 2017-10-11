from django.shortcuts import render_to_response

from login.models import Account

def login(request):
    	return render_to_response('login/index.html')	#Relative templates location added to avoid confusion