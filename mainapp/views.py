from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from mainapp.models import *
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.template import loader
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import *
from django.contrib.auth.forms import *
from .models import *
from .forms import *
from .models import GamesType
from .forms import GamesTypeForm
from .models import Result
from .forms import ResultForm

def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def aboutme(request):
    template = loader.get_template('aboutme.html')
    context = {}
    return HttpResponse(template.render(context, request))


def computer(request):
    template = loader.get_template('Computer.html')
    context = {'Computer':Computer.objects.all(),'title': 'Данные об компьютере','power_user': request.user.groups.filter(name='TEST').exists()}
    return HttpResponse(template.render(context, request))

def game(request):
    template = loader.get_template('Game.html')
    context = {'Game':Game.objects.all(),'title': 'Данные об игре','power_user': request.user.groups.filter(name='TEST').exists()}
    return HttpResponse(template.render(context, request))

def gamestype(request):
    template = loader.get_template('GamesType.html')
    context = {'GamesType':GamesType.objects.all(),'title': 'Данные об типе игры','power_user': request.user.groups.filter(name='TEST').exists()}
    return HttpResponse(template.render(context, request))

def player(request):
    template = loader.get_template('Player.html')
    context = {'Player':Player.objects.all(),'title': 'Данные об игроке','power_user': request.user.groups.filter(name='TEST').exists()}
    return HttpResponse(template.render(context, request))

def result(request):
    template = loader.get_template('Result.html')
    context = {'Result':Result.objects.all(),'title': 'Данные об результатах','power_user': request.user.groups.filter(name='TEST').exists()}
    return HttpResponse(template.render(context, request))

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        form = UserCreationForm()

    template = loader.get_template('UserForm.html')
    context = {
        'form': form,
        'title': 'Регистрация пользователя'
    }
    return HttpResponse(template.render(context, request))

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            userpass = form.cleaned_data['password']
            user = authenticate(username=username, password=userpass)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

    else:
        form = AuthenticationForm()

    template = loader.get_template('UserForm.html')
    context = {
        'form': form,
        'title': 'Вход в систему'
    }
    return HttpResponse(template.render(context, request))

def logout_user(request):
    logout(request)
    messages.success(request, 'Вы вышли из системы')
    return HttpResponseRedirect(reverse('index'))

def new_computer(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ComputerForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('computer'))
        else:
            form = ComputerForm()

        template = loader.get_template('ComputerForm.html')
        context = {
        'form': form,
        'title': 'добавление компьютера'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")

def edit_computer(request, kp):
    if request.user.is_authenticated:
        try:
            computer = Computer.objects.get(id=kp)
        except Computer.DoesNotExist:
            raise Http404("Данные компьютера с кодом" + str(kp) + " не найден")

        if request.method == 'POST':
            form = ComputerForm(request.POST, instance=computer)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('computer'))
        else:
            form = ComputerForm(instance=computer)

        template = loader.get_template('ComputerForm.html')
        context = {
        'form': form,
        'title': 'редактирование компьютера'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")
def del_computer(request, kp):
    if request.user.is_authenticated:
        try:
            computer = Computer.objects.get(id=kp)
        except Computer.DoesNotExist:
            raise Http404("Данные компьютера с кодом" + str(kp) + " не найден")
        m = f"Данные компьютера {Computer.name} удалёны"
        computer.delete()
        messages.error(request, m)
        return HttpResponseRedirect(reverse('computer'))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")


def new_game(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = GameForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('game'))
        else:
            form = GameForm()

        template = loader.get_template('GameForm.html')
        context = {
            'form': form,
            'title': 'добавление игры'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")


def edit_game(request, kp):
    if request.user.is_authenticated:
        try:
            game = Game.objects.get(id=kp)
        except Game.DoesNotExist:
            raise Http404("Данные игры с кодом" + str(kp) + " не найден")

        if request.method == 'POST':
            form = GameForm(request.POST, instance=computer)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('game'))
        else:
            form = ComputerForm(instance=game)

        template = loader.get_template('GameForm.html')
        context = {
            'form': form,
            'title': 'редактирование игры'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")


def del_game(request, kp):
    if request.user.is_authenticated:
        try:
            game = Game.objects.get(id=kp)
        except Game.DoesNotExist:
            raise Http404("Данные игры с кодом" + str(kp) + " не найден")
        m = f"Данные игры {Computer.name} удалёны"
        game.delete()
        messages.error(request, m)
        return HttpResponseRedirect(reverse('game'))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")

def new_player(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PlayerForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('player'))
        else:
            form = PlayerForm()

        template = loader.get_template('PlayerForm.html')
        context = {
            'form': form,
            'title': 'добавление игрока'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")


def edit_player(request, kp):
    if request.user.is_authenticated:
        try:
            player = Player.objects.get(id=kp)
        except Player.DoesNotExist:
            raise Http404("Данные игрока с кодом" + str(kp) + " не найден")

        if request.method == 'POST':
            form = PlayerForm(request.POST, instance=player)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('player'))
        else:
            form = PlayerForm(instance=player)

        template = loader.get_template('PlayerForm.html')
        context = {
            'form': form,
            'title': 'редактирование игрока'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")


def del_player(request, kp):
    if request.user.is_authenticated:
        try:
            player = Player.objects.get(id=kp)
        except Player.DoesNotExist:
            raise Http404("Данные игрока с кодом" + str(kp) + " не найден")
        m = f"Данные игрока {Player.name} удалёны"
        player.delete()
        messages.error(request, m)
        return HttpResponseRedirect(reverse('player'))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")


def new_gamestype(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = GamesTypeForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('gamestype'))
        else:
            form = GamesTypeForm()

        template = loader.get_template('GamesTypeForm.html')
        context = {
            'form': form,
            'title': 'добавление типа игры'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")


def edit_gamestype(request, kp):
    if request.user.is_authenticated:
        try:
            gamestype = GamesType.objects.get(id=kp)
        except GamesType.DoesNotExist:
            raise Http404("Данные игрока с кодом" + str(kp) + " не найден")

        if request.method == 'POST':
            form = GamesTypeForm(request.POST, instance=gamestype)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('gamestype'))
        else:
            form = GamesTypeForm(instance=gamestype)

        template = loader.get_template('GamesTypeForm.html')
        context = {
            'form': form,
            'title': 'редактирование игрока'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")


def del_gamestype(request, kp):
    if request.user.is_authenticated:
        try:
            gamestype = GamesType.objects.get(id=kp)
        except GamesType.DoesNotExist:
            raise Http404("Данные типа игры с кодом" + str(kp) + " не найден")
        m = f"Данные типа игры {GamesType.name} удалёны"
        gamestype.delete()
        messages.error(request, m)
        return HttpResponseRedirect(reverse('gamestype'))
    else:
        return HttpResponseForbidden("<h1 align = 'center'>Оплати интернет дурачек</h1>")

def new_result(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ResultForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('result'))
        else:
            form = ResultForm()

        template = loader.get_template('ResultForm.html')
        context = {
            'form': form,
            'title': 'добавление результата'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1 align='center'>Заплати интеренет дурачок!</h1>")

def edit_result(request, kp):
    if request.user.is_authenticated:
        try:
            result = Result.objects.get(id=kp)
        except Result.DoesNotExist:
            raise Http404("Результат с кодом" + str(kp) + " не найден")

        if request.method == 'POST':
            form = ResultForm(request.POST, instance=result)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('result'))
        else:
            form = ResultForm(instance=result)

        template = loader.get_template('ResultForm.html')
        context = {
            'form': form,
            'title': 'редактирование результата'
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseForbidden("<h1 align='center'>Заплати интеренет дурачок!</h1>")

def del_result(request, kp):
    if request.user.is_authenticated:
        try:
            result = Result.objects.get(id=kp)
        except Result.DoesNotExist:
            raise Http404("Результат с кодом" + str(kp) + " не найден")
        m = f"Результат {Result.name} удалён"
        result.delete()
        messages.error(request, m)
        return HttpResponseRedirect(reverse('result'))
    else:
        return HttpResponseForbidden("<h1 align='center'>Заплати интеренет дурачок!</h1>")