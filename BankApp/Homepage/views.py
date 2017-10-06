from django.shortcuts import render_to_response


#from models import posts
from Homepage.models import posts

def index(request):
    	return render_to_response('Homepage/index.html')	#Relative templates location added to avoid confusion

def login(request):
    	return render_to_response('Homepage/login.html')	#Relative templates location added to avoid confusion

def transfer(request):
	return render_to_response('Homepage/transfer.html')	#Relative templates location added to avoid confusion