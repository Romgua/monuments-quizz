from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .forms import MonumentNameForm
from django.http import HttpResponseRedirect

from .models import Monument
# Create your views here.

def index(request):
    return render(request, 'quizz/index.html')

def detail(request):
    if request.method == 'POST':
        form = MonumentNameForm(request.POST)
        if form.is_valid():
            request.method = 'GET'
            monument = Monument.objects.get(id=request.POST.get('monument_id'))
            if monument.name.lower() == request.POST.get('monument_name').lower():
                request.user.add_experience(monument)
                request.user.register_done(monument)
                request.user.save()
            return detail(request)
    else:
        todo_monuments = request.user.get_todo_monuments()
        monument = todo_monuments.first()
        form = MonumentNameForm()
        context = {
            'user': request.user,
            'monument': monument,
            'form': form,
        }
        if monument:
            real_url = monument.image.url.split("/")
            real_url = '/' + '/'.join(real_url[1:])

    return render(request, 'quizz/detail.html', context)