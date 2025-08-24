from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'complete_status', 'due_date']
        widgets = {
            'created_date': forms.DateTimeInput(attrs={
               'type': 'datetime-local'
            }),
            
            'due_date': forms.DateTimeInput(attrs={
                'type': 'datetime-local'
            }),
        }
