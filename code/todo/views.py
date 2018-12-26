from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.
def todoview(request):
	all = TodoItem.objects.all()
	return render(request,'todo.html',
				  {'all_items':all})
				  
				  
				  
def addTodo(request):
	#create a new todo all_items
	new_item = TodoItem(content=request.POST['content'])
	#save
	new_item.save()
	#redirect the browser to  '/todo/'
	return HttpResponseRedirect('/todoview/')
	
	
def deleteTodo(request, todo_id):
	#get id from request
	item_to_delete = TodoItem.objects.get(id=todo_id)
	#delete id 
	item_to_delete.delete()
	#return todoview page
	return HttpResponseRedirect('/todoview/')
	