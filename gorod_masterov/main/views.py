from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
# Create your views here.
def index(request):
    if request.method=='POST':
        form = TaskForm(request.POST)
        form.save()
    tasks = Task.objects.all
    form = TaskForm()
    return render(request,'main/index.html',{'title': "Main page",'tasks': tasks, 'form': form})

def about(request):
    return render(request,"main/about.html")

