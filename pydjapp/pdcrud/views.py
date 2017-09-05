from django.shortcuts import render
from django.http import HttpResponseRedirect

#Import form and model for further use in view
from .forms import ThoughtForm
from .models import Thoughts


# Create your views here.
def index(request):
    # Either serve html page with empty form (GET) or create new table entry (POST)
    #if request.method == 'POST':
    #    form = ThoughtForm(request.POST)  # Save POSTed form data as form
    #    if form.is_valid():  # Check data validity
    #        # Create new table entry from cleaned form data
    #        thought = Thought(title=form.cleaned_data['title'],
    #                          thought=form.cleaned_data['thought'])
    #        thought.save()  # Save new table entry to table/DB
    #        return HttpResponseRedirect('/')  # Redirect (GET) to domain root
    #else:
    #    form = ThoughtForm()  # Form, to be served to template when rendering it

    # Render template, serve it an empty form instance
    return render(request, 'pdcrud/index.html')

#
def create(request):
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
        form = ThoughtForm()  # Form, to be served to template when rendering it

    return render(request, 'pdcrud/create.html', {'form': form})
