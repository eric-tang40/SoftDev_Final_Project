from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Pokemon
import requests

class PokemonListView(ListView):
    model = Pokemon

def indv_page(request, poke_id):
    poke_data = get_pokemon_data(poke_id)

    pokemon_obj, created = Pokemon.objects.get_or_create(
        name=poke_data['name'],
        defaults={'types': [t['type']['name'] for t in poke_data['types']], 'base_stats': {stat['stat']['name']: stat['base_stat'] for stat in poke_data['stats']}}
    )

    context = {'poke_data': poke_data}
    return render(request, 'pokemon/page.html', context)

def index(request):
    url = "https://pokeapi.co/api/v2/pokemon?limit=151"  
    response = requests.get(url)
    data = response.json()
    pokemon_names = [pokemon['name'] for pokemon in data.get('results', [])]

    for pokemon_name in pokemon_names:
        pokemon_data = get_pokemon_data(pokemon_name)
        pokemon_obj, created = Pokemon.objects.get_or_create(
            name=pokemon_data['name'],
            defaults={'types': [t['type']['name'] for t in pokemon_data['types']], 'base_stats': {stat['stat']['name']: stat['base_stat'] for stat in pokemon_data['stats']}}
        )

    context = {'pokemon_list': pokemon_names}
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

for pokemon_details in pokemon_list:
    print(f"Name: {pokemon_details['name']}")
    print(f"Types: {pokemon_details['types']}")
    print(f"Abilities: {pokemon_details['abilities']}")
    print("Base Stats:")
    for stat, value in pokemon_details['base_stats'].items():
        print(f"  {stat}: {value}")
    print("\n" + "="*40 + "\n") 
