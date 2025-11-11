from django.db import models

class Especie(models.Model):
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


class Animal(models.Model):
    apelido = models.CharField(max_length=100, blank=True, null=True)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    raca = models.CharField(max_length=100)
    anos = models.IntegerField(default=0)
    meses = models.IntegerField(default=0)
    status = models.CharField(max_length=50, default="disponivel")
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.apelido or f"Animal {self.id}"
