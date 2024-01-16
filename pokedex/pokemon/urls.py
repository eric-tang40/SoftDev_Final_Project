from django.urls import path
from .views import index, indv_page

app_name = 'pokemon'

urlpatterns = [
    path('', index, name='index'), 
    path('<int:poke_id>', indv_page, name='indv_page'), 
]
