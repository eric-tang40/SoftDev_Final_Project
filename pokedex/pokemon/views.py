from django.shortcuts import render

def index(request):
    return render(request, 'pokemon/index.html')