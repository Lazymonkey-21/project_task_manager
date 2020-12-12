from django.contrib import admin
from .models import Project,Task

#Registering models (Project,Task) into admin
admin.site.register(Project)
admin.site.register(Task)

#Super User

#username - swapnil
#pass - 1234