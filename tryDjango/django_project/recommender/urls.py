from django.urls import path
from . import views

# Empty path means that it's just in homepage.
urlpatterns = [
    path('', views.home, name='recommender-home'),
    path('about/', views.about, name='recommender-about'),
]