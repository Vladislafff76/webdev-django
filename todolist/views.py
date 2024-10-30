from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoItem

# Create your views here.

def todoView(request):
    all_todo = TodoItem.objects.all()
    return render(request, 'todolist.html', {'all_items': all_todo})

def addTodoView(request):
    x = request.POST['content']
    new_item = TodoItem(content = x)
    new_item.save()
    return HttpResponseRedirect('/todo/')

def deleteTodoView(request, i):
    y = TodoItem.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/todo/')