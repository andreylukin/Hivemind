from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import loader

def index(request):
	return HttpResponse("Hey there")
# Create your views here.
#


