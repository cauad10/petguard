from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Animal

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return render(request, "petguard/login.html")


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url="login")
def index(request):
    return render(request, "petguard/index.html")


def add_animal(request):
    anos = range(1, 11)
    meses = range(1, 13)
    return render(request, 'petguard/addAnimal.html', {'anos': anos, 'meses': meses})

def detalhes(request, id):
    animal = get_object_or_404(Animal, id=id)
    return render(request, "petguard/detalhes.html", {"animal": animal})

def listar_animais(request):
    animais = Animal.objects.all().values("id", "especie", "raca", "idade", "status")
    return JsonResponse(list(animais), safe=False)
