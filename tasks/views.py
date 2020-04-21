from django.shortcuts import render
from django.http import HttpResponse

from tasks.models import Task
from tasks.forms import TaskForm
from django.shortcuts import redirect
# Create your views here.

def index(request):
    consulta = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'info':consulta,'temp':form}
    return render(request,"tasks/list.html", context)
