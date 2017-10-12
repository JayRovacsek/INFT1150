from django.shortcuts import render_to_response


def index(request):
    	return render_to_response('account/index.html')	#Relative templates location added to avoid confusion