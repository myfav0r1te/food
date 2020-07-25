from django.shortcuts import render,redirect, get_object_or_404
from django.utils import timezone
from .models import Food
from .forms import NewBlog

def welcome(request):
    return render(request, 'viewcrud/index.html')

def read(request):
    foods= Food.objects.all()
    return render(request, 'viewcrud/funccrud.html', {'foods':foods})

def create(request):
    if request.method == 'POST':
        form = NewBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('food')
    else:
        form = NewBlog()
        return render(request, 'viewcrud/new.html', {'form':form})

def update(request,pk):
    food = get_object_or_404(Food, pk=pk)

    form = NewBlog(request.POST, instance=food)

    if form.is_valid():
        form.save()
        return redirect('food')

    return render(request, 'viewcrud/new.html', {'form':form})

    
def delete(request,pk):
    food = get_object_or_404 (Food, pk = pk)
    food.delete()
    return redirect ('food')

# Create your views here.
