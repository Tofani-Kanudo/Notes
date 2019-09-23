from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .models import TodoItem
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    all=TodoItem.objects.all()
    return render(request,'hii.html',{'all_items':all})
def addTodo(request):
    new=TodoItem(content=request.POST['content'])
    new.save()
    return HttpResponseRedirect('/todo/')
def deleteTodo(request, todo_id):
    itemdel = TodoItem.objects.get(id=todo_id)
    itemdel.delete()
    return HttpResponseRedirect('/todo/')