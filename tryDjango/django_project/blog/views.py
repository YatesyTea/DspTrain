from django.shortcuts import render

posts = [
    {
        'author': 'DYates',
        'title': 'Blog Post 1',
        'content': 'First post mate',
        'date': 'January 10, 2020'
    },
    {
        'author': 'DYates',
        'title': 'Blog Post 2',
        'content': 'Second post mate',
        'date': 'January 10, 2020'
    }
]

def home(request):
    context = {
        'posts': posts,
        'title' : 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})