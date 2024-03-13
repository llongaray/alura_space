from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages
from apps.galeria.forms import FotografiaForms

def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado!')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_hora").filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado!')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_hora").filter(publicada=True)
    if "buscar" in request.GET:
        nome_buscar = request.GET['buscar']
        if nome_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_buscar)

    return render(request, "galeria/buscar.html", {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuario não logado!')
        return redirect('login')
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request):
    pass

def deletar_imagem(request):
    pass