from django.shortcuts import render, redirect
from .forms import TagForm, NoteForm
from .models import Tag


# Create your views here.
def main(request):
    return render(request, 'noteapp/index.html')

def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/tag.html', {'form': form})

    return render(request, 'noteapp/tag.html', {'form': TagForm()})

def note(request):
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save()
            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_note.tags.add(tag)
            return redirect(to='noteapp:main')
        else:
            return render(request, 'noteapp/note.html', {"tags":tags, "form": form })



    return render(request, 'noteapp/note.html', {"tags":tags, "form": NoteForm()})