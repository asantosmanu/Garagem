from django.db import models

class acessorio (models.Model):
    descricao = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.descricao