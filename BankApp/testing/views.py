from django.shortcuts import render_to_response

# Create your views here.
def index(request):
	return render_to_response('testing/home.html')	#Relative templates location added to avoid confusion