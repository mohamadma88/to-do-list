from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def addtask(request):
    form = TaskForm()
    task = Task.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Task.objects.create(title=cd['title'])
        return redirect('/')
    return render(request, 'home/index.html', {'tasks': task, 'form': form})


def deleteTask(request,pk):
    todo = Task.objects.get(pk=pk)
    if request.method == 'POST':
        todo.delete()
        return redirect('/')
    return render(request, 'home/delete.html', {'todo': todo})
