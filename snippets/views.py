from django.shortcuts import render
from django.http import HttpResponse


def snippet_list(request):
    context = {
        'names': ['bob', 'jerry', 'tamara']
    }
    return render(request, 'snippets/home.html', context)


def snippet_detail(request, id):
    return HttpResponse(f'snippet details {id}')