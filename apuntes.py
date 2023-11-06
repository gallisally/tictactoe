python3 -m venv env 
source env/bin/activate 
pip install django
django-admin startproject core .
python manage.py startapp tictactoe