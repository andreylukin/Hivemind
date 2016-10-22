from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers

from .models import Building

def index(request):
    return HttpResponse("Hey there")

def allBuildingLocation(request):
    output = serializers.serialize('json', Building.objects.all())
    return HttpResponse(output)



