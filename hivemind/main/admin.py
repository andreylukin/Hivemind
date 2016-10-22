from django.contrib import admin

# Register your models here.
from .models import *


admin.site.register(Entity)
admin.site.register(Classes)
admin.site.register(Entity_Class)
admin.site.register(Building)
admin.site.register(StudySession)
