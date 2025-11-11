from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Animal, Especie


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
    return redirect("login")


@login_required(login_url="login")
def index(request):
    animais = Animal.objects.all()
    return render(request, "petguard/index.html", {"animais": animais})


@login_required(login_url="login")
def add_animal(request, id=None):
    animal = None
    if id:
        animal = get_object_or_404(Animal, id=id)

    especies = Especie.objects.all()

    if request.method == 'POST':
        anos = request.POST.get('anos')
        meses = request.POST.get('meses')
        apelido = request.POST.get('apelido')
        especie_id = request.POST.get('especie')
        raca = request.POST.get('raca')
        status = request.POST.get('status')
        observacoes = request.POST.get('observacoes')

        especie = get_object_or_404(Especie, id=especie_id)

        if animal:
            animal.anos = anos
            animal.meses = meses
            animal.apelido = apelido
            animal.especie = especie
            animal.raca = raca
            animal.status = status
            animal.observacoes = observacoes
            animal.save()
        else:
            Animal.objects.create(
                anos=anos,
                meses=meses,
                apelido=apelido,
                especie=especie,
                raca=raca,
                status=status,
                observacoes=observacoes,
            )
        return redirect('index')

    anos = range(0, 11)
    meses = range(0, 13)

    return render(request, 'petguard/addAnimal.html', {
        'animal': animal,
        'anos': anos,
        'meses': meses,
        'especies': especies,
    })


@login_required(login_url="login")
def detalhes(request, id):
    animal = get_object_or_404(Animal, id=id)
    return render(request, "petguard/detalhes.html", {"animal": animal})


@login_required(login_url="login")
def listar_animais(request):
    animais = Animal.objects.all().values("id", "especie__nome", "raca", "anos", "meses", "status")
    lista = []
    for a in animais:
        idade_formatada = ""
        if a["anos"] > 0:
            idade_formatada += f'{a["anos"]} ano(s)'
        if a["meses"] > 0:
            idade_formatada += f' e {a["meses"]} mês(es)'
        if not idade_formatada:
            idade_formatada = "0 mês(es)"
        lista.append(
            {
                "id": a["id"],
                "especie": a["especie__nome"],
                "raca": a["raca"],
                "idade": idade_formatada,
                "status": a["status"],
            }
        )
    return JsonResponse(lista, safe=False)


@require_POST
@login_required(login_url="login")
def excluir_animal(request, animal_id):
    try:
        animal = Animal.objects.get(id=animal_id)
        animal.delete()
        return JsonResponse({"success": True})
    except Animal.DoesNotExist:
        return JsonResponse({"success": False, "error": "Animal não encontrado"})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)})
