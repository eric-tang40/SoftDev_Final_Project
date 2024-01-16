from django.shortcuts import render
from .models import Pokemon
from django.views.generic import ListView
from django.http import JsonResponse
import json
import requests

class PokemonListView(ListView):
    model = Pokemon

def index(request, poke_id):
    poke_data = get_pokemon_data(poke_id)
    context = {'poke_data': poke_data}
    return render(request, 'pokemon/index.html', context)

def get_pokemon_data(poke_id):
    # fetching data
    poke_API = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    response = requests.get(poke_API)
    data = response.json()
    return data

