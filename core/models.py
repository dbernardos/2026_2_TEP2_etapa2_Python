# core/models.py
from django.db import models

class Tweet(models.Model):
    # Sobrescrevendo o id padrão para usar o id do dataset
    id = models.IntegerField(primary_key=True, verbose_name="ID do Tweet")
    keyword = models.CharField(max_length=50, null=True, blank=True, verbose_name="Palavra-chave")
    location = models.CharField(max_length=100, null=True, blank=True, verbose_name="Localização")
    text = models.TextField(verbose_name="Texto do Tweet")
    target = models.IntegerField(verbose_name="Alvo (0=Não, 1=Sim)")

    class Meta:
        db_table = 'disaster_tweets'
        ordering = ['id']
        verbose_name = 'Tweet de Desastre'
        verbose_name_plural = 'Tweets de Desastres'

    def __str__(self):
        # Retorna uma string amigável para o admin e shells do Django
        label = "Desastre" if self.target == 1 else "Normal"
        return f"[{self.id}] ({label}) {self.text[:40]}..."
