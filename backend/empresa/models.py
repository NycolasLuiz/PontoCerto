from django.db import models

class Empresa (models.Model):
    cnpj = models.CharField(max_length=18, primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100, unique=True)
    data_fundacao =models.DateField(("Data criação"), auto_now=False, auto_now_add=False)
  
    
    def __str__(self):
        return self.nome    
    
