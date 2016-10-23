from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers

from .models import *


def getAllBuildingLocations(request):
    output = serializers.serialize('json', Building.objects.all())
    return HttpResponse(output)

def getSessions(request,classesneeded):
    output = serializers.serialize('json', StudySession.objects.filter(classes = classesneeded))
    return HttpResponse(output)

def getUserClasses(request, user):
    return HttpResponse(serializers.serialize('json', Classes.objects.filter(entity=user)))

def createNewSession(request, user, building, classes):
    session = StudySession(building = Building.objects.get(pk = int(building)), classes = Classes.objects.get(pk = int(classes)))
    session.save()
    session.entities.add(Entity.objects.get(pk = int(user)))
    return HttpResponse(building)

def joinSession(request, user, session):
    joinsession = StudySession.objects.get(pk = int(session))
    Entity.objects.get(pk = int(user)).honey = 5 + Entity.objects.get(pk = int(user)).honey
    joinsession.entities.add(Entity.objects.get(pk = int(user)))
    return HttpResponse(serializers.serialize('json', StudySession.objects.filter(building = joinsession.building, classes = joinsession.classes)))

def leaveSession(request, user, session):
    leavesession = StudySession.objects.get(pk = int(session))
    leavesession.entities.remove(Entity.objects.get(pk = int(user)))
    if (StudySession.objects.get(pk = int(session)).entities).count() == 0:
        StudySession.objects.get(pk = int(session)).delete()

def nameEntity(request, user):
     return HttpResponse(Entity.objects.get(pk = int(user)).name)

def nameBuilding(request, building):
    return HttpResponse(Building.objects.get(pk = int(building)).name)

def nameClass(request, classes):
    return HttpResponse(Classes.objects.get(pk = int(classes)).name)

def addClassUser(request, user, classes):
    student = Entity.objects.get(pk = int(user))
    student.classes.add(Classes.objects.get(pk = int(classes)))

def honeyEntity(request, user):
    return HttpResponse(Entity.objects.get(pk = int(user)).honey)

def honeyAllEntity(request):
    return HttpResponse(serializers.serialize('json', (Entity.objects.all()).order_by('-honey')))

