from django.forms import ModelForm
from . import models

class ComputerForm(ModelForm):
    class Meta:
        model = models.Computer
        fields = [ 'name', 'configuration']

class GameForm(ModelForm):
    class Meta:
        model = models.Game
        fields = [ 'name', 'game_type' ]

class GamesTypeForm(ModelForm):
    class Meta:
        model = models.GamesType
        fields = [ 'name']

class PlayerForm(ModelForm):
    class Meta:
        model = models.Player
        fields = [ 'name','rating']

class ResultForm(ModelForm):
    class Meta:
        model = models.Result
        fields = [ 'computer','game', 'player']