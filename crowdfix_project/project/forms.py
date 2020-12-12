from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Task
class DateInput(forms.DateInput):
    input_type='date'

    
#Custom form to pass widget date in the form. 
class TaskForm(forms.ModelForm):
    start = forms.DateField(widget=DateInput)
    end = forms.DateField(widget=DateInput)
    #Passing the format of field
    class Meta:
        model = Task
        fields= ['name','description','start','end','task_id']