from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')

    completed = request.POST.get('newsletter_topimage')


    context = { 'tasks': tasks, 'form': form}
    return render(request, 'list.html', context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'update_task.html', context)


def taskDelete (rquest, pk):
    item = Task.objects.get(id=pk)
    item.delete()
    return redirect('/')


def taskTicked (rquest, pk):
    item = Task.objects.get(id=pk)
    item.complete = True
    item.save()
    return redirect('/')


def taskUnticked (rquest, pk):
    item = Task.objects.get(id=pk)
    item.complete = False
    item.save()
    return redirect('/')


def searchView (request):
    query = request.POST.get('searchquery')
    object_list = Task.objects.filter(title__icontains=query)
    context = {'object_list': object_list, 'query': query,}
    return render(request, 'search.html', context)