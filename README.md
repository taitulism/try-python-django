# Todos API
## Just me trying out Python/Django...



## Todo Model
* title
* details
* completed

### **RUN SERVER**
```sh
$ py manage.py runserver
```
> command might vary: `py/python/python3` depending on environment

## API
* Get all todos  
GET http://127.0.0.1:8000/todos/

* Create a Todo item  
POST http://127.0.0.1:8000/todos/ + request body {title: 'bla', details: 'bla bla'}

* Edit a Todo item  
PUT http://127.0.0.1:8000/todos/<id\> + request body {completed: True} also for changing title/details

* Delete a Todo item  
DELETE http://127.0.0.1:8000/todos/<id\>
