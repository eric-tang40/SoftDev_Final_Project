from django.urls import path
from .views import index

app_name = 'pokemon'

urlpatterns = [
    path('', index, name='index'), 
]
