from django.shortcuts import render
from .models import Player, Game
from django.core.serializers.json import json, DjangoJSONEncoder


def join(request):
    if request.POST:
        json_body = json.dumps(request.BODY)
        username = json_body['username']
        gamename = json_body['gamename']
        game = Game.objects.get_or_create(name=gamename)
        player = Player(name=username)
        player.save()
        game.player_set.add(player)
        return json.dumps(game, cls=DjangoJSONEncoder)
