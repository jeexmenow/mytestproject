from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Jeex',
        'title': 'Test post',
        'content': 'some text',
        'date_posted': 'date posted'
    },
    {
        'author': 'Not Jeex, just user',
        'title': 'Test post2',
        'content': 'some text',
        'date_posted': 'date posted'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'meets/home.html', context)


def about(request):
    return render(request, 'meets/about.html', {'title': 'О клубе Python Bytes'})