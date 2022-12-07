from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse, request
from .models import Todo
from .forms import ToDoForm
from django.contrib.auth.decorators import login_required

def home(request):
    all = Todo.objects.all()
    return render(request, 'todo/home.html', {'todos':all})


def detail(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    return render(request, 'todo/detail.html', {'todo':todo})


def delete(request, todo_id):
    if not request.user.is_authenticated:
        messages.error(request, 'Login First', 'warning')
        return redirect('accounts:login')
    todo = get_object_or_404(Todo, id=todo_id)
    todo.delete()
    messages.success(request, 'Todo Deleted Successfully', 'warning')
    return redirect('todo:home')


def create(request):
    if request.method == 'GET':
        if not request.user.is_authenticated:
            messages.error(request, 'Login First', 'warning')
            return redirect('accounts:login')        
        form = ToDoForm()
        return render(request, 'todo/create.html', {'form':form})
    
    else:
        if not request.user.is_authenticated:
            messages.error(request, 'Login First', 'warning')
            return redirect('accounts:login')  
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Todo created successfully', 'success')
            return redirect('todo:home')
        else:
            return HttpResponse(f'{form.errors}')

@login_required(login_url='accounts:login')
def update(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id)
    if request.method == 'GET':
        form = ToDoForm(instance=todo)
        return render(request, 'todo/update.html', {'form':form})
    else:
        form = ToDoForm(data=request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'your todo updated successfully', 'success')
            return redirect('todo:detail', todo_id)
