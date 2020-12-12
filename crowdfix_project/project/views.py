from django.shortcuts import render
from django.views.generic import (ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)
from .models import Project,Task
from .forms import TaskForm


# Project classes

#Listing All the projects
class ProjectListView(ListView):
    model = Project
    context_object_name = 'projects'
    template_name='project/home.html'

#Detailed view of individual project
class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tasks"] = Task.objects.all()
        return context
    
#Project Creation
class ProjectCreateView(CreateView):
    model = Project
    fields =['title','description','duration']
    def form_valid(self,form):
        return super().form_valid(form)

#Project Updation
class ProjectUpdateView(UpdateView):
    model = Project
    fields =['title','description','duration']

    #Accessing same form created in CreateView by UpdateView
    def form_valid(self,form):
        return super().form_valid(form)

#Deleting the project
class ProjectDeleteView(DeleteView):
    model = Project
    success_url = '/'  #redirection to home page

#Task Classes

#Listing All the tasks under specific project
class TaskDetailView(DetailView):
    model = Task
    template_name = 'project/task_detail.html'
    def get_context_data(self, **kwargs):  
        context = super().get_context_data(**kwargs)
        x= self.kwargs['pk1']
        context["tasks"] = Task.objects.filter(id=x) #filtering on the basis task id
        return context

#Creating task inside the projects
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm  #Passing custom designed from forms.py 
    success_url=''
    def form_valid(self,form):
        return super().form_valid(form)

#Updating projects 
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    #Accessing same form created in CreateView by UpdateView
    def form_valid(self,form):
        return super().form_valid(form) 

#Deleting the task ,Redirect to home page
class TaskDeleteView(DeleteView):
    model = Task
    success_url = '/'

def about(request):
    return render(request,'project/about.html',{'title':'about'})