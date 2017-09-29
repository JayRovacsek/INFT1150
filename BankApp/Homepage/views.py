from django.shortcuts import render_to_response


#from models import posts
from Homepage.models import posts

def index(request):
	return render_to_response('index.html')