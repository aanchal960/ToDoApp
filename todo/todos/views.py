from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
from .models import Todo
from .forms import TodoForm

# Create your views here.


def home(request):
    notes = Todo.objects.all()
    template = loader.get_template('note.html')

    form = TodoForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    context = {
        'notes': notes,
        'form': form
    }
    return render(request, 'note.html', context)
    # return render(request, 'note.html', { 'notes': notes, 'form':form })

# return render_to_response("note.html", notes)
