from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Classes(models.Model):
        name = models.CharField(max_length = 30)

        def __str__(self):
            return self.name

class Entity(models.Model):
        name = models.CharField(max_length = 30)
        email = models.CharField(max_length = 30)
        password = models.CharField(max_length = 30, default = 'password')
        classes = models.ManyToManyField(Classes, blank = False)
        honey = models.IntegerField(default = 0)

        def __str__(self):
            return self.name

class Building(models.Model):
        name = models.CharField(max_length = 2000)
        longitude = models.FloatField(default = 0)
        latitude= models.FloatField(default = 0)

        def __str__(self):
            return self.name

class StudySession(models.Model):
        entities = models.ManyToManyField(Entity, blank = False)
        building = models.ForeignKey(Building)

        def __str__(self):
            return self.entities.name + " " + self.building.name
