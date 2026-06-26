from django.contrib.auth import logout
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ParticipanteForm, EventoForm
from .models import Participante, Evento


def index(request):
    return render(request, 'index.html')


def login_view(request):
    return render(request, 'login.html')


def cadastro_view(request):
    return render(request, 'cadastro.html')


def eventos(request):
    busca = request.GET.get('busca', '')
    eventos = Evento.objects.all()
    if busca:
        eventos = eventos.filter(Q(nome__icontains=busca) | Q(local__icontains=busca))

    form = EventoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('eventos')

    return render(request, 'gerenciamento/eventos.html', {
        'eventos': eventos,
        'form': form,
        'busca': busca,
    })


def participantes(request):
    busca = request.GET.get('busca', '')
    participantes = Participante.objects.select_related('evento').all()
    if busca:
        participantes = participantes.filter(
            Q(nome__icontains=busca) | Q(email__icontains=busca) | Q(evento__nome__icontains=busca)
        )

    form = ParticipanteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('participantes')

    return render(request, 'gerenciamento/participantes.html', {
        'participantes': participantes,
        'form': form,
        'busca': busca,
    })


def editar_participante(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)
    form = ParticipanteForm(request.POST or None, instance=participante)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('participantes')

    return render(request, 'gerenciamento/editar_participante.html', {
        'form': form,
        'participante': participante,
    })


def excluir_participante(request, participante_id):
    participante = get_object_or_404(Participante, id=participante_id)

    if request.method == 'POST':
        participante.delete()
        return redirect('participantes')

    return render(request, 'gerenciamento/excluir_participante.html', {
        'participante': participante,
    })


def editar_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)
    form = EventoForm(request.POST or None, instance=evento)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('eventos')

    return render(request, 'gerenciamento/editar_evento.html', {
        'form': form,
        'evento': evento,
    })


def excluir_evento(request, evento_id):
    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        evento.delete()
        return redirect('eventos')

    return render(request, 'gerenciamento/excluir_evento.html', {
        'evento': evento,
    })


def logout_view(request):
    logout(request)
    return render(request, 'index.html')
