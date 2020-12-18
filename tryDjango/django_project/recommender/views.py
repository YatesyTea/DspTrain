from django.shortcuts import render

recipes = [
    {
        'author': 'DYates',
        'title': 'Curried Goat',
        'content': 'Please Love This',
        'date': 'January 10, 2020'
    },
    {
        'author': 'FHassan',
        'title': 'Shakshuka',
        'content': 'Just add cumin!',
        'date': 'February 29, 2021'
    }
]

def home(request):
    context = {
        'recipes': recipes,
        'title' : 'Home'
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})