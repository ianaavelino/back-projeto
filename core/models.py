from django.db import models


class Evento(models.Model):
    nome = models.CharField('Nome', max_length=160)
    descricao = models.TextField('Descrição', blank=True)
    data = models.DateField('Data')
    horario = models.TimeField('Horário', blank=True, null=True)
    local = models.CharField('Local', max_length=160, blank=True)
    vagas = models.PositiveIntegerField('Quantidade de vagas', default=0)
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-data', 'nome']

    def __str__(self):
        return self.nome


class Participante(models.Model):
    nome = models.CharField('Nome', max_length=120)
    email = models.EmailField('Email', max_length=254)
    telefone = models.CharField('Telefone', max_length=30, blank=True)
    evento = models.ForeignKey(Evento, verbose_name='Evento', on_delete=models.PROTECT, related_name='participantes')
    criado_em = models.DateTimeField('Criado em', auto_now_add=True)

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
        ordering = ['-criado_em']

    def __str__(self):
        return self.nome

