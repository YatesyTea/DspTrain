from django.shortcuts import render

recipes = [
    {
        'title': 'Lentil Apple and Turkey Wrap',
        'calories': 200,
        'fat': 10,
        'protein': 10,
        'sodium': 10,
        'ingredients': 'Chicken Mate',
        'directions': '1: Chop stuff',
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