from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Главная страница")

def data(request):
    return HttpResponse("Вторая страница")
def test(request):
    return HttpResponse("Тест страница")
