from django.db import models
from django.contrib.auth.models import User


class Config_horario(models.Model):
    horario_entrada_1=models.TimeField(blank=True, null=True)
    horario_saida_1=models.TimeField(blank=True, null=True)
    horario_entrada_2 =models.TimeField(blank=True, null=True)
    horario_saida_2 =models.TimeField(blank=True, null=True)



class Cargo(models.Model):
    cargo=models.CharField("Cargo do funcionário", max_length=70)

    def __str__(self):
        return self.cargo

class Funcionario(models.Model):
    usuario= models.OneToOneField(User, on_delete=models.CASCADE,
        verbose_name='Usuario')
    nome=models.CharField('Nome',max_length=128)
    data_de_nascimento=models.DateTimeField('data de nascimento',blank=True,null=True)
    telefone_celular=models.CharField("Telefone Celular", max_length=15, help_text='Numero de telefone celular no formato (99)99999-9999', null=True, blank=True)
    email=models.EmailField('E-mail',null=True, blank=True)
    cargo=models.ForeignKey(Cargo,on_delete=models.SET_NULL, blank=True, null=True)
    supervisor = models.ForeignKey('Funcionario', on_delete=models.SET_NULL, blank=True, null=True)
    config_horario=models.ForeignKey(Config_horario,on_delete=models.SET_NULL, blank=True, null=True)


    def __str__ (self):
        return self.nome

class status(models.Model):
    nome=models.CharField(max_length=30)

    def __str__ (self):
        return self.nome


class Frequencia(models.Model):
    data=models.DateField()
    horario_entrada_1=models.TimeField(null=True)
    horario_saida_1=models.TimeField(null=True)
    horario_entrada_2=models.TimeField(null=True)
    horario_saida_2=models.TimeField(null=True)
    justificativa=models.TextField(null=True,blank=True)

    def set_horario_entrada(self, horario):
        self.horario_entrada_1 = horario




