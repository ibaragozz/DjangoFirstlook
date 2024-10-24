from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Это мой первый проект на Django</h1>")

def new(request):
    return HttpResponse("<h1>Это моя вторая страница на Django</h1>")

def data(request):
    return HttpResponse("<h1>Это все ради изучения Django</h1>")

def test(request):
    return HttpResponse("<h1>Привет человеку, проверяющему мое ДЗ =)</h1>")

