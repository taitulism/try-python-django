from django.shortcuts import render
from django.http import HttpResponse, QueryDict
from django.http.response import HttpResponseNotFound
# from django.core import serializers
from .models import Todo
import json


def get_create_todo (req):
    if req.method == 'GET':
        # todos = serializers.serialize('json', Todo.objects.all())
        todos = list(Todo.objects.all().values())

        return HttpResponse(json.dumps(todos), 'application/json')
    
    elif req.method == 'POST':
        newTodo = Todo.objects.create(title = req.POST['title'], details = req.POST['details'], completed = False)

        return HttpResponse(newTodo.pk)
    

def edit_delete_todo (req, id):
    if req.method == 'DELETE':
        try:
            Todo.objects.get(id = id).delete()
            return HttpResponse('ok')
        
        except Exception as err:
            print(err)
            return HttpResponseNotFound('Todo #' + id + ' Not Found')

    elif req.method == 'PUT':
        putData = QueryDict(req.body)

        try:
            existingTodo = Todo.objects.get(id = id)
            if putData.get('title'):
                existingTodo.title = putData.get('title')
            if putData.get('details'):
                existingTodo.details = putData.get('details')
            if putData.get('completed'):
                existingTodo.completed = putData.get('completed')

            existingTodo.save()
            return HttpResponse('ok')

        except Exception as err:
            print('Handling run-time error:', err)
            return HttpResponseNotFound('Todo #' + id + ' Not Found')
