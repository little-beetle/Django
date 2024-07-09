from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse, HttpRequest
from .forms import UserBioForm
def day_index(request: HttpRequest):
    pretty_words = [
        'A', 'B', 'C', 'D'
    ]

    context = {
        'pretty_words': pretty_words
    }

    return render(request, 'happy_day/day-index.html', context=context)



def greeting(request: HttpRequest):
    return render(request, 'happy_day/greeting.html')

def win(request: HttpRequest):
    return render(request, 'happy_day/win.html')


def postcard(request: HttpRequest) -> HttpResponse:
    context = {
        'form': UserBioForm(),
    }
    return render(request, 'happy_day/create-postcard.html', context=context)

