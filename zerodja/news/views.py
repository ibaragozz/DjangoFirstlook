from django.shortcuts import render, redirect
from .models import NewsPost
from .forms import NewsPostForm

# Create your views here.
def home(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена неверно'
    form = NewsPostForm()
    return render(request, 'news/create.html', {'form': form, 'error': error})
