from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .forms import MonumentNameForm
from django.http import HttpResponseRedirect

from .models import Monument
from .constants import FAKE_CITIES_LIST, EXPERIENCE_MODE_VALUES

import random

# Create your views here.


def index(request):
    return render(request, 'quizz/index.html')


def detail(request):
    if request.method == 'POST':
        form = MonumentNameForm(request.POST)
        if form.is_valid():
            request.method = 'GET'
            monument = Monument.objects.get(id=request.POST.get('monument_id'))
            if monument.city.lower() == request.POST.get('monument_name').lower():
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

def jeu(request):
    if request.method == 'POST':
        # form = MonumentNameForm(request.POST)
        # if form.is_valid():
        request.method = 'GET'
        monument = Monument.objects.get(id=request.POST.get('monument_id'))
        response = (request.POST.get('monument_name') 
                        if request.POST.get('monument_name') 
                        else request.POST.get('monument_name_text'))
        if monument.city.lower() == response.lower():
            xp_count = EXPERIENCE_MODE_VALUES.get(request.POST.get('mode'))
            request.user.add_experience(monument, xp_count)
        request.user.register_done(monument)
        request.user.save()
        nb_question = int(request.POST.get('numberQuestion'))
        if not nb_question:
            nb_question = 0
        if nb_question >= 10:
            nb_ok = request.user.user_monuments.filter(done=True).count()
            context = {
                'user': request.user,
                'nb_done': nb_ok,
            }
            return render(request, 'quizz/end.html', context)
        return jeu(request)
    else:
        todo_monuments = request.user.get_todo_monuments()
        monument = todo_monuments.first()
        if not monument:
            nb_ok = request.user.user_monuments.filter(done=True).count()
            context = {
                'user': request.user,
                'nb_done': nb_ok,
            }
            return render(request, 'quizz/end.html', context)
        form = MonumentNameForm()
        choice_carre = []
        choice_duo = []
        # Remplissage de la liste pour carré
        for i in range(3):
            to_check_city = random.choice(FAKE_CITIES_LIST)
            while to_check_city == monument.city:
                to_check_city = random.choice(FAKE_CITIES_LIST)
            choice_carre.append(to_check_city)
        to_check_city = random.choice(FAKE_CITIES_LIST)
    
        # Remplissage de la liste pour duo
        while to_check_city == monument.city:
            to_check_city = random.choice(FAKE_CITIES_LIST)
        choice_duo.append(to_check_city)

        # On ajoute le vrai choix
        choice_carre.append(monument.city)
        choice_duo.append(monument.city)

        # On mélange
        random.shuffle(choice_carre)
        random.shuffle(choice_duo)

        context = {
            'user': request.user,
            'monument': monument,
            'form': form,
            'choice_carre': choice_carre,
            'choice_duo': choice_duo,
        }
        if monument:
            real_url = monument.image.url.split("/")
            real_url = '/' + '/'.join(real_url[1:])

    return render(request, 'quizz/jeu.html', context)