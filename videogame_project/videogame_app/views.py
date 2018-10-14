from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import GameIdea
from .forms import gameentry



def listing(request):

    posts = GameIdea.objects.filter(published_date__lte=timezone.now()).order_by('currentdate')
    return render(request,'videogame_app/Add.html', {'post' : posts})

def post_edit(request,pk):
    post = get_object_or_404(gameentry,pk=pk)
    if request.method == "POST":
        form = GameIdea(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.currentdate = timezone.now()
            post.save()
        return redirect('post_detail', pk=post.pk)


    else:

        form=GameIdea(instance=post)

    return render(request, 'videogame_app/Edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(gameentry, pk=pk)
    return render(request, 'videogame_app/index.html', {'post': post})

def post_new(request):

    if request.method == "POST":
        form = GameIdea(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.currentdate = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = GameIdea()
        return render(request,'videogame_app/Edit.html', {'form': form})

