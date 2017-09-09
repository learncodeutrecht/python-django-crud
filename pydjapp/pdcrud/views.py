"""views for the CRUD actions."""
from django.shortcuts import render
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
    form = ThoughtForm()

    return render(request,
                  'pdcrud/thoughtForm.html',
                  {'form': form,
                   'title': 'Update thought.',
                   'url': '/update/' + str(id)})


def readall(request):
    """REAL ALL existing thoughts and show them on the HTML page."""
    thoughts = Thoughts.objects.all()
    # thoughts = []
    return render(request, 'pdcrud/thoughts.html', {'thoughts': thoughts})
