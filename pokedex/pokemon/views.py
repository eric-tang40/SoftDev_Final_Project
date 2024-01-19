from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Pokemon
from django.urls import reverse
import requests

class PokemonListView(ListView):
    model = Pokemon

def indv_page(request, poke_id):
    pokemon_obj = Pokemon.objects.get(dex_num=poke_id)

    context = {'poke_data': pokemon_obj}
    return render(request, 'pokemon/page.html', context)

def index(request):
    pokemon_objects = Pokemon.objects.all()

    pokemon_list = [
        {
            'name': pokemon.name,
            'types': pokemon.types,
            'base_stats': pokemon.base_stats,
            'ability': pokemon.ability,
            'url': reverse('pokemon:indv_page', args=[pokemon.dex_num])  
        }
        for pokemon in pokemon_objects
    ]

    context = {'pokemon_list': pokemon_list}
    return render(request, 'pokemon/index.html', context)

def get_pokemon_data(poke_id):
    poke_API = f"https://pokeapi.co/api/v2/pokemon/{poke_id}"
    response = requests.get(poke_API)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

pokemon_list = []

for poke_id in range(1, 152):
    pokemon_data = get_pokemon_data(poke_id)
    
    if pokemon_data:
        pokemon_details = {
            'name': pokemon_data['name'],
            'types': [t['type']['name'] for t in pokemon_data['types']],
            'abilities': [ability['ability']['name'] for ability in pokemon_data['abilities']],
            'base_stats': {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}
        }
        
        pokemon_list.append(pokemon_details)
    else:
        print(f"Pokemon with ID {poke_id} not found.")