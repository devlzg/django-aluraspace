from django.db import models

# Aqui é onde ficam os "models", que são classes python que serão traduzidas para tabelas
# em um banco de dados (através do ORM)

class Fotografia(models.Model):
  
  OPCOES_CATEGORIA = [
    ("NEBULOSA", "Nebulosa"), # tem que ser tupla pois o método CharField() só entende tuplas
    ("ESTRELA", "Estrela"),
    ("GALÁXIA", "Galáxia"),
    ("PLANETA", "Planeta")
  ]
  
  nome = models.CharField(max_length=100, null=False, blank=False) # campo de caractere na tabela
  legenda = models.CharField(max_length=150, null=False, blank=False)
  categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
  descricao = models.TextField(null=False, blank=False) # campo de texto, ideal para textos grandes
  foto = models.CharField(max_length=100, null=False, blank=False)
  
  def __str__(self): 
    return f"Fotografia [nome={self.nome}]"