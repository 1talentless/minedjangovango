from django.db import models
class Computer(models.Model):
    name = models.CharField(max_length=50)
    configuration = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class GamesType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Game(models.Model):
    name = models.CharField(max_length=50)
    game_type = models.ForeignKey(GamesType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
class Player(models.Model):
    rating = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Result(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return self.game.name + '/' + self.computer.name + '(' +str(self.player) + ')'
