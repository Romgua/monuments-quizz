from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse

from .models import Monument
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the monument index.")

def detail(request):
    try:
        monument = Monument.objects.first()
    except monument.DoesNotExist:
        raise Http404("Question does not exist")
    context = {
        'monument': monument,
    }
    if monument.image:
        real_url = monument.image.url.split("/")
        real_url = '/' + '/'.join(real_url[1:])
        context.update({'real_url' : real_url})
    return render(request, 'quizz/detail.html', context)