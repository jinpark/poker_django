from django.db import models
from django.auth.user.models import User

suits = ["S", "H", "D", "C"]
# 1 = Ace, 11 = Jack etc
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"];
full_deck = [x+y for x in suits for y in ranks]
full_deck_string = ",".join(full_deck)

# class Player(model.Model):
#     user = models.OneToOneField(User)
#     game = models.ForeignKey(User)
#     money = models.FloatField(default=2.0)

class Player(models.Model):
    name = models.CharField(max_length=100)
    game = models.ForeignKey(Game)
    money = models.FloatField(default=2.0)
    hand = models.CharField(max_length=10)

class Game(models.Model):
    name = models.CharField(max_length=200, unique=True)
    deck = models.CharField(max_length=200, default=full_deck_string)
    board = models.CharField(max_length=100)
    players = models.ForeignKey(Player)
    pot = models.FloatField(default=0)
    turn = models.IntegerField(default=0)
    started = models.BooleanField(defaut=False)
    max_players = models.IntegerField(default=2)

