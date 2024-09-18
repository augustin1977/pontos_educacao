from django.db import models

class Familia (models.Model):
    nome_familia=models.CharField(max_length=300)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Familia:{self.nome_familia}"
class Pessoa (models.Model):
    familia=models.ForeignKey(Familia, on_delete=models.CASCADE,blank=False,null=False)
    nome=models.CharField(max_length=300,blank=False,null=False)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    email=models.EmailField(unique=True,blank=False,null=False)
    senha=models.CharField(max_length=64,blank=False,null=False)
    responsavel=models.BooleanField(blank=False,null=False)
    
    def __str__(self):
        return f"Nome:{self.nome}, {str(self.familia)}"

class Pontos(models.Model):
    filho=models.ForeignKey(Pessoa,on_delete=models.CASCADE)
    motivo=models.TextField()
    quantidade=models.DecimalField(max_digits=5, decimal_places=2)
    data_ponto=models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"filho:{self.filho.nome}, pontos:{str(self.quantidade)} data={self.data_ponto}, motivo:{self.motivo}"
    
