from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("aboutme/", views.aboutme, name='aboutme'),
    path("computer/", views.computer, name='computer'),
    path("game/", views.game, name="game"),
    path("gamestype/", views.gamestype, name="gamestype"),
    path("player/", views.player, name="player"),
    path("result/", views.result, name="result"),

    path("player/news/", views.new_player, name="new_player"),
    path("player/<int:kp>/edit/", views.edit_player, name="edit_player"),
    path("player/<int:kp>/delete/", views.del_player, name="del_player"),

    path("game/news/", views.new_game, name="new_game"),
    path("game/<int:kp>/edit/", views.edit_game, name="edit_game"),
    path("game/<int:kp>/delete/", views.del_game, name="del_game"),

    path("computer/news/", views.new_computer, name="new_computer"),
    path("computer/<int:kp>/edit/", views.edit_computer, name="edit_computer"),
    path("computer/<int:kp>/delete/", views.del_computer, name="del_computer"),

    path("result/news/", views.new_result, name="new_result"),
    path("result/<int:kp>/edit/", views.edit_result, name="edit_result"),
    path("result/<int:kp>/delete/", views.del_result, name="del_result"),

    path("gamestype/news/", views.new_gamestype, name="new_gamestype"),
    path("gamestype/<int:kp>/edit/", views.edit_gamestype, name="edit_gamestype"),
    path("gamestype/<int:kp>/delete/", views.del_gamestype, name="del_gamestype"),
path("register/", views.register_user, name='register'),
    path("login/", views.login_user, name='login'),
    path("logout/", views.logout_user, name='logout'),
]



