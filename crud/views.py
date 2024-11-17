from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Import the Player model
from .models import Player

# Create your views here.
def index(request):
    context = {}
    # Get all the players from the database
    list_players = Player.objects.all()
    template = loader.get_template("index.html")
    # Add the players to the context
    context = {
        'list_players': list_players
    }
    return HttpResponse(template.render(context,request))

def view_player(request, player_id):
    # Get the player with the given id
    detail_player = Player.objects.get(id= player_id)

    # Render the player detail template
    template = loader.get_template("detail.html")

    # Add the player to the context
    context = {
        'player': detail_player
    }
    return HttpResponse(template.render(context,request))