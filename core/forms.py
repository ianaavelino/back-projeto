from django import forms
from .models import Participante, Evento


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nome', 'email', 'telefone', 'evento']
        labels = {
            'nome': 'Nome',
            'email': 'Email',
            'telefone': 'Telefone',
            'evento': 'Evento',
        }
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome do participante',
                'class': 'campo-input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email do participante',
                'class': 'campo-input'
            }),
            'telefone': forms.TextInput(attrs={
                'placeholder': 'Telefone do participante',
                'class': 'campo-input'
            }),
            'evento': forms.Select(attrs={
                'class': 'campo-input'
            }),
        }


class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'descricao', 'data', 'horario', 'local', 'vagas']
        labels = {
            'nome': 'Nome',
            'descricao': 'Descrição',
            'data': 'Data',
            'horario': 'Horário',
            'local': 'Local',
            'vagas': 'Quantidade de vagas',
        }
        widgets = {
            'nome': forms.TextInput(attrs={
                'placeholder': 'Nome do evento',
                'class': 'campo-input'
            }),
            'descricao': forms.Textarea(attrs={
                'placeholder': 'Descrição do evento',
                'class': 'campo-input',
                'rows': 4,
            }),
            'data': forms.DateInput(attrs={
                'type': 'date',
                'class': 'campo-input'
            }),
            'horario': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'campo-input'
            }),
            'local': forms.TextInput(attrs={
                'placeholder': 'Local do evento',
                'class': 'campo-input'
            }),
            'vagas': forms.NumberInput(attrs={
                'placeholder': 'Quantidade de vagas',
                'class': 'campo-input'
            }),
        }
