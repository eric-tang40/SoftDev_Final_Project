from django.shortcuts import render
from .models import Pokemon
from django.views.generic import ListView
from django.http import JsonResponse
import json
import requests

class PokemonListView(ListView):
    model = Pokemon

def indv_page(request, poke_id):
    poke_data = get_pokemon_data(poke_id)
    context = {'poke_data': poke_data}
    return render(request, 'pokemon/page.html', context)

def index(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"  
    response = requests.get(url)
    data = response.json()
    pokemon_names = []
    pokemon_names = [pokemon['name'] for pokemon in data.get('results', [])]

    context = {'pokemon_list': pokemon_names}
    return render(request, 'pokemon/index.html', context)


def get_pokemon_data(poke_id):
    # fetching data
    poke_API = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    response = requests.get(poke_API)
    data = response.json()
    return data


