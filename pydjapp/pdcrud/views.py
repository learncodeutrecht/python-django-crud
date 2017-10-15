"""views for the CRUD actions."""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# Import form and model for further use in view
from .forms import TaskForm
from .models import Task


def index(request):
    """Create your views here."""
    # Render template, serve it an empty form instance
    return render(request, 'pdcrud/index.html')


def create(request):
    """GET and POST for the Create Form for creating TASKS."""
    if request.method == 'POST':
        form = TaskForm(request.POST)  # Save POSTed form data as form
        if form.is_valid():  # Check data validity
            # Create new table entry from cleaned form data
            task = Task(title=form.cleaned_data['title'],
				description=form.cleaned_data['description'],
				date=form.cleaned_data['date'],
				deadline=form.cleaned_data['deadline'],
				urgent=form.cleaned_data['urgent'],
				important=form.cleaned_data['important'],)
            task.save()  # Save new table entry to table/DB
            return HttpResponseRedirect('/')  # Redirect (GET) to domain root
    else:
        form = TaskForm()  # Form, to be served to template when rendering

    return render(request,
                  'pdcrud/taskForm.html',
                  {'form': form,
                   'title': 'Create a new task.',
                   'url': '/create/'})


def update(request, id):
    """Update a single record."""
    if request.method == 'GET':
        
       
        task = Task.objects.get(id=id)
        form = TaskForm(task.__dict__)

        return render(request,
                    'pdcrud/taskForm.html',
                    {'form': form,
                    'title': 'Update task.',
                    'url': '/update/' + str(id) +"/"}
                    )
    elif request.method == "POST":
        print("log update:" + request.method)
        print(request.POST)
        form = TaskForm(request.POST)
        if form.is_valid():
            task = Task.objects.get(id=id)
            task.task = form.cleaned_data['task']
            task.tasktype  = form.cleaned_data['tasktype']
            task.author  = form.cleaned_data['author']
            task.date  = form.cleaned_data['date']
            task.save()
            return HttpResponseRedirect("/readall/")
        else:
            return render(request,
                    'pdcrud/taskForm.html',
                    {'form': form,
                    'title': 'Update task.',
                    'url': '/update/' + str(id) +"/"}
                    )

def readall(request):
    """REAL ALL existing tasks and show them on the HTML page."""
    tasks = Task.objects.all()
    # tasks = []
    return render(request, 'pdcrud/tasks.html', {'tasks': tasks})

def delete(request, id):
    """Delete the record with ID received in request"""
    print(id)
    
    Task.objects.filter(id=id).delete()
    """fetch remaining records"""
    tasks = Task.objects.all()
    return render(request, 'pdcrud/tasks.html', {'tasks': tasks})

