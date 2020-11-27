from django.shortcuts import render

posts = [
    {
        'author': 'DYates',
        'title': 'blogpost1',
        'content': 'First post mate',
        'date': 'January 10, 2020'
    },
    {
        'author': 'DYates',
        'title': 'blogpost2',
        'content': 'Second post mate',
        'date': 'January 10, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')