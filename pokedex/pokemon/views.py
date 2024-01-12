from django.shortcuts import render
from .models import Pokemon
from django.views.generic import ListView

class PokemonListView(ListView):
    model = Pokemon

def index(request):
    return render(request, 'pokemon/index.html')