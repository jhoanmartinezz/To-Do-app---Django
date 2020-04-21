from django.shortcuts import render
from django.http import HttpResponse

from tasks.models import Task
from tasks.forms import TaskForm
# Create your views here.

def index(request):
    consulta = Task.objects.all()
    form = TaskForm()
    context = {'info':consulta,'temp':form}
    return render(request,"tasks/list.html", context)
