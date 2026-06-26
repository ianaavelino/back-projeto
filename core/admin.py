from django.contrib import admin
from .models import Participante, Evento


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data', 'local', 'vagas', 'criado_em')
    search_fields = ('nome', 'local')
    list_filter = ('data',)


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'evento', 'criado_em')
    search_fields = ('nome', 'email', 'evento__nome')
    list_filter = ('evento',)
