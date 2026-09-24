from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from core.models import Evento, Participante


@login_required
def dashboard(request):
    total_eventos = Evento.objects.count()
    total_participantes = Participante.objects.count()

    return render(request, 'dashboard/dashboard.html', {
        'total_eventos': total_eventos,
        'total_participantes': total_participantes,
    })