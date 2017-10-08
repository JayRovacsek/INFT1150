from django.shortcuts import render_to_response


#from models import posts
from homepage.models import posts

def notAuthed(request):
    	return render_to_response('homepage/notAuthed.html')	#Relative templates location added to avoid confusion

def login(request):
    	return render_to_response('homepage/login.html')	#Relative templates location added to avoid confusion

def transfer(request):
	return render_to_response('homepage/transfer.html')	#Relative templates location added to avoid confusion

def account(request):
	return render_to_response('homepage/account.html')	#Relative templates location added to avoid confusion