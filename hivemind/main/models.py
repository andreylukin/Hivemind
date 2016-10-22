from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Entity(models.Model):
        name = models.CharField(max_length = 30)
        email = models.CharField(max_length = 30)
        password = models.CharField(max_length = 30, default = 'password')

        def __str__(self):
            return self.name

class Classes(models.Model):
        name = models.CharField(max_length = 30)

        def __str__(self):
            return self.name

class Entity_Class(models.Model):
        entity = models.ForeignKey(Entity)
        classes = models.ForeignKey(Classes)
        karma = models.IntegerField(default = 0)

class Building(models.Model):
        name = models.CharField(max_length = 2000)
        longitude = models.FloatField(default = 0)
        latitude= models.FloatField(default = 0)

        def __str__(self):
            return self.name

class StudySession(models.Model):
        entities = models.ManyToManyField(Entity_Class, blank = False)
        building = models.ForeignKey(Building)

        def __str__(self):
            return self.entities.name + " " + self.building.name
