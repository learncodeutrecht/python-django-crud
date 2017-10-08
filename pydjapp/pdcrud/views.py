"""views for the CRUD actions."""
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

# Import form and model for further use in view
from .forms import ThoughtForm
from .models import Thoughts


def index(request):
    """Create your views here."""
    # Render template, serve it an empty form instance
    return render(request, 'pdcrud/index.html')


def create(request):
    """GET and POST for the Create Form for creating THOUGHTS."""
    if request.method == 'POST':
        form = ThoughtForm(request.POST)  # Save POSTed form data as form
        if form.is_valid():  # Check data validity
            # Create new table entry from cleaned form data
            thought = Thoughts(thought=form.cleaned_data['thought'],
                               thoughttype=form.cleaned_data['thoughttype'],
                               author=form.cleaned_data['author'],
                               date=form.cleaned_data['date'])
            thought.save()  # Save new table entry to table/DB
            return HttpResponseRedirect('/')  # Redirect (GET) to domain root
    else:
        form = ThoughtForm()  # Form, to be served to template when rendering

    return render(request,
                  'pdcrud/thoughtForm.html',
                  {'form': form,
                   'title': 'Create a new thought.',
                   'url': '/create/'})


def update(request, id):
    """Update a single record."""
    if request.method == 'GET':
        
       
        thought = Thoughts.objects.get(id=id)
        form = ThoughtForm(thought.__dict__)

        return render(request,
                    'pdcrud/thoughtForm.html',
                    {'form': form,
                    'title': 'Update thought.',
                    'url': '/update/' + str(id) +"/"}
                    )
    elif request.method == "POST":
        print("log update:" + request.method)
        print(request.POST)
        form = ThoughtForm(request.POST)
        if form.is_valid():
            thought = Thoughts.objects.get(id=id)
            thought.thought = form.cleaned_data['thought']
            thought.thoughttype  = form.cleaned_data['thoughttype']
            thought.author  = form.cleaned_data['author']
            thought.date  = form.cleaned_data['date']
            thought.save()
            return HttpResponseRedirect("/readall/")
        else:
            return render(request,
                    'pdcrud/thoughtForm.html',
                    {'form': form,
                    'title': 'Update thought.',
                    'url': '/update/' + str(id) +"/"}
                    )

def readall(request):
    """REAL ALL existing thoughts and show them on the HTML page."""
    thoughts = Thoughts.objects.all()
    # thoughts = []
    return render(request, 'pdcrud/thoughts.html', {'thoughts': thoughts})

def delete(request, id):
    """Delete the record with ID received in request"""
    print(id)
    
    Thoughts.objects.filter(id=id).delete()
    """fetch remaining records"""
    thoughts = Thoughts.objects.all()
    return render(request, 'pdcrud/thoughts.html', {'thoughts': thoughts})

def select_single_thought(request):
	"""select a single thought"""
	single_thought = Thoughts.objects.all()
	return render(request, 'pdcrud/select_single_thought.html', {'single_thought': single_thought})

def view_single_thought(request, id):
	""""READ a single tought"""
	single_thought = get_object_or_404(Thoughts, pk=id)
	return render(request, 'pdcrud/single_thought.html', {'single_thought' : single_thought})

def delete_thought(request):
	"""Select which thoughts to delete"""
	thoughts = Thoughts.objects.all()
	return render(request, 'pdcrud/delete_thought.html', {'thoughts': thoughts})

def update_thought(request):
	"""Select which thoughts to update"""
	thoughts = Thoughts.objects.all()
	return render(request, 'pdcrud/update_thought.html', {'thoughts': thoughts})
