from django.urls import path,include
from tictactoe.views import *

urlpatterns = [
    path("",index),
    path("tictactoe/<int:id>/<str:name>/",game)
]