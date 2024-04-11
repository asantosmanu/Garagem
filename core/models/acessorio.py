from django.db import models

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100, null=True)


    def __str__(self):
        return f"{self.descricao} - {self.id}"
    