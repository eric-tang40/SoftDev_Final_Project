# SoftDev_Final_Project

PROJECT NAME: POKEDEX

Roster:
Eric Tang (Project Manager)
Farhan Khan
Tyler Chan
Kanjuda Shaika

Description:
Website about the original 151 pokemon. There are three apps: pokemon, trainer, teams. Pokemon contains a table of all 151 pokemon. Each pokemon has an individual html page, which is shown on the table. There is a search bar for the user. Trainer contains a list of 7 trainers and their info. Teams allows you to choose a trainer and see which pokemon are on their "team". 

APIs: https://pokeapi.co/api/v2/pokemon?limit=151 


Launch Codes:
To setup packages: 
  Build Packages: 
    pip install --upgrade pip-tools pip setuptools wheel
    pip-compile --upgrade --generate-hashes --output-file requirements_env/main.txt requirements_env/main.in
    pip-compile --upgrade --generate-hashes --output-file requirements_env/dev.txt requirements_env/dev.in

  Install Packages:
    pip-sync requirements_env/main.txt (for production)
    pip-sync requirements_env/main.txt requirements_env/dev.txt (for development)


  Mac users may need to locally install the following packages (with pip install)
    pip install pgadmin4
    pip install requests
    Pip install psycopg2

  To run the server:
    1. Create virtual environment, activate it 
    2. IMPORTANT: go to /trainers/models.py. Uncomment all code beginning with “Trainer.objects.create(“
    3. Make migrations (python manage.py makemigrations) and migrate (python manage.py migrate)
    4. Go back to /trainers/models.py. Comment out or remove all code beginning with  “Trainer.objects.create(“
    5. Update secrets.json with necessary information
    6. Runserver (python manage.py runserver)


