from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .froms import TaskForm

# Create your views here.
def read(request):
    tasks = Task.objects.all()
    return render(request, 'read.html', {'tasks':tasks})

def create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
    else:
        form = TaskForm()
    return render(request, 'create.html', {'form':form})

def update(request, pk):
    task = get_object_or_404(Task, pk = pk)
    form = TaskForm(request.POST or None, instance= task)
    if form.is_valid():
        form.save()
        return redirect('read')

    return render(request, 'update.html', {'form':form})

def delete(request, pk):
    task = get_object_or_404(Task, pk= pk)
    if request.method == 'POST':
        task.delete()
        return redirect('read')
    return render(request, 'delete.html', {'task': task})

def description_view(request, pk):
    task = get_object_or_404(Task, pk= pk)
    return render(request, 'description_view.html', {'task': task})