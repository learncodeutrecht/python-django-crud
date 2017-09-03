from django.shortcuts import render
from django.http import HttpResponseRedirect


from .forms import ThoughtForm
from .models import Thought


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = ThoughtForm(request.POST)
        if form.is_valid():
            # Have form saved as model instance in DB
            thought = Thought(title=form.cleaned_data['title'],
                              thought=form.cleaned_data['thought'])
            thought.save()
            return HttpResponseRedirect('/')
    else:
        form = ThoughtForm()

    return render(request, 'pdcrud/index.html', {'form': form})
