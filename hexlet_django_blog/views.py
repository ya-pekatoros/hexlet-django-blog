from django.shortcuts import render


def index(request):
    return render(request, 'index.html', context={
        'who': 'Yaroslav',
    })


def about(request):
    return render(request, 'about.html')
