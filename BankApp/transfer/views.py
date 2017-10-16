from django.shortcuts import render_to_response

# Create your views here.

def index(request):
	return render_to_response('transfer/index.html')	#Relative templates location added to avoid confusion

def maketransfer(request):
	return render_to_response('transfer/maketransfer.html')	#Relative templates location added to avoid confusion