from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.core import serializers
import json
from django.core.serializers.json import DjangoJSONEncoder

from .models import *
from scipy.spatial import Voronoi, voronoi_plot_2d, KDTree
import numpy as np

# array of centers of sites of interest - read out of table in db
array = []
locations = Building.objects.all()
for all in locations:
    array2 = [0,0]
    array2[0] = all.latitude
    array2[1] = all.longitude
    array.append(array2)

points = np.array(array)

# library that creates a map between point in x-y space and nearest site
tree = KDTree(points)

# returns index of site in above array that is closest to x-y point

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
    honey=Entity.objects.get(pk = int(user))
    honey.honey=  honey.honey + 10
    honey.save()
    return HttpResponse(session.id)

def joinSession(request, user, session):
    joinsession = StudySession.objects.get(pk = int(session))
    honey=Entity.objects.get(pk = int(user))
    honey.honey=  honey.honey + 5
    honey.save()
    joinsession.entities.add(Entity.objects.get(pk = int(user)))
    return HttpResponse(serializers.serialize('json', StudySession.objects.filter(building = joinsession.building, classes = joinsession.classes)))

def leaveSession(request, user, session):
    leavesession = StudySession.objects.get(pk = int(session))
    leavesession.entities.remove(Entity.objects.get(pk = int(user)))
    if (StudySession.objects.get(pk = int(session)).entities).count() == 0:
        StudySession.objects.get(pk = int(session)).delete()
    return HttpResponse("leaveSession")

def nameEntity(request, user):
     return HttpResponse(Entity.objects.get(pk = int(user)).name)

def nameBuilding(request, building):
    return HttpResponse(Building.objects.get(pk = int(building)).name)

def nameClass(request, classes):
    return HttpResponse(Classes.objects.get(pk = int(classes)).name)

def allnameClass(request):
    object = Classes.objects.values('name', 'id')
    return HttpResponse(json.dumps(list(object), cls=DjangoJSONEncoder))

def addClassUser(request, user, classes):
    student = Entity.objects.get(pk = int(user))
    student.classes.add(Classes.objects.get(pk = int(classes)))
    return HttpResponse("Hey")

def honeyEntity(request, user):
    return HttpResponse(Entity.objects.get(pk = int(user)).honey)

def honeyAllEntity(request):
    return HttpResponse(serializers.serialize('json', (Entity.objects.all()).order_by('-honey')))

def getClosest(request, latitude, longitude):
    return HttpResponse((tree.query([float(latitude), float(longitude)])[1])+1)


def getSessionUser(request, user):
    query_set = (StudySession.objects.filter(entities = int(user)))
    if len(query_set)<1:
        return HttpResponse('-1')
    else:
	return HttpResponse(query_set[0].id)


def chatEmail(request, session):
    query_set = StudySession.objects.filter(entities = int(session))
    #users = query_set.entities
 #   return HttpResponse(query_set[0].entities)
    return HttpResponse(StudySession.objects.get(id = session).entities.all())
