from django.shortcuts import render

# Create your views here.

def index(request):
    	return render_to_response('transfer/index.html')	#Relative templates location added to avoid confusion