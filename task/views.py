from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Task
from .forms import TaskForm

# Create your views here.

def task_list(request):
    # save the form data
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')   
    else:
        form = TaskForm()
    
    # Get the query from the saerch form
    query = request.GET.get('q') 
    if query:
        tasks = Task.objects.filter(title__icontains=query)
    else: 
        # If no query, then display all tasks
        tasks = Task.objects.all()

    return render(request, 'task_list.html', {'tasks': tasks, 'form': form})

# def task_create(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('task_list')
#     else:
#         form = TaskForm()
#     return render(request, 'task_list.html', {'form': form})

# update the task
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task_update.html', {'form': form, 'task': task})

# delete the task
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect('task_list')

# toggle the status of the task from 'Pending' to 'Completed' and vice versa
def toggle_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.status == 'Completed':
        task.status = 'Pending'
    else:
        task.status = 'Completed'
    task.save()
    return redirect('task_list')