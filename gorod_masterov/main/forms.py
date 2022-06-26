from .models import Task
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["number", "name"]
        widgets = {"number": TextInput(attrs={'class': 'form-control', 'placeholder': "input number"}),
                   "name": TextInput(attrs={'class': 'form-control', 'placeholder': "input name"})}
