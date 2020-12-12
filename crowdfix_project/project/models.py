from django.db import models
from django.urls import reverse
from django.utils import timezone


#Project page  database model (fields = [title,description,duration]) 
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration =models.IntegerField(default=34)

    def __str__(self):
        return self.title
    #to return to address after (Project creation,updation)
    def get_absolute_url(self):
        return reverse("project-detail", kwargs={"pk": self.pk})

#Project page  database model (fields = [name , description , start , end , task_id(foreign_key) ]) 
class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start = models.DateField()
    end = models.DateField()
    task_id = models.ForeignKey('Project',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    #to return to address after ( Task creation , updation )
    def get_absolute_url(self):
        return reverse("task-detail", kwargs={"pk":self.task_id.id,"pk1":self.pk})