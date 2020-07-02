from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    local = models.TextField(blank=True, null=True, max_length=50)
    data_evento = models.DateTimeField(verbose_name='Data do Evento', null=True)
    data_criacao = models.DateField(auto_now=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'evento'

    def __str__(self):
        return self.titulo
    #def get_data_evento(self):
    #   return self.data_evento.strftime('%Y/%m/%dT%H:%M Hrs')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H%M')