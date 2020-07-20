from django.shortcuts import render,redirect,get_object_or_404
from .models import Post, Human
from .forms import CreateForm
from random import choice
# Create your views here.
def layout(request):
    return render(request, 'blog/layout.html')


def board(request):
    nuna = Post.objects.all()
    hoho = Human.objects.all()
    return render(request, 'blog/board.html', {'nuguri':nuna,'human':hoho})

def create(request):
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.food = choice(['고구마라떼','계란빵','떡볶이','치킨','삼겹살'])
            form.save()
            return redirect('board')
    else:
        form = CreateForm()
        return render(request, 'blog/main.html', {'form':form})

def update(request,pk):
    human_post = get_object_or_404(Human, pk=pk)
    if request.method == "POST":
        form = CreateForm(request.POST, instance=human_post)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            return redirect('board')
    else:
        form = CreateForm(instance=human_post)
        return render(request, 'blog/main.html', {'form':form})

def delete(request, pk):
    post = get_object_or_404(Human, pk=pk)
    post.delete()
    return redirect('board')