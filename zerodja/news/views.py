from django.shortcuts import render
from .models import NewsPost
from .forms import NewsPostForm

# Create your views here.
def home(request):
    news = NewsPost.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create(request):
    form = NewsPostForm()
    return render(request, 'news/create.html', {'form': form})
