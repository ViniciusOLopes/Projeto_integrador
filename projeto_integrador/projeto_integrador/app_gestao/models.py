from django.db import models

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    CPF = models.TextField(max_length=255)
    RG = models.TextField(max_length=255)
    Orgao = models.TextField(max_length=255)
    Emissao = models.DateField()  # Corrigido
    Cidade_Nascimento = models.TextField(max_length=255)
    Estado = models.TextField(max_length=255)
    Data_Nascimento = models.DateField()  # Corrigido
    Endereco = models.TextField(max_length=255)
    Setor_Bairro = models.TextField(max_length=255)
    Quadra = models.TextField(max_length=255)
    Lote = models.TextField(max_length=255)
    Apartamento = models.TextField(max_length=255)
    Complemento = models.TextField(max_length=255)
    Cidade = models.TextField(max_length=255)
    CEP = models.IntegerField()  # Corrigido
    Estado = models.TextField(max_length=255)
    Telefone = models.TextField(max_length=255)
    Email = models.TextField(max_length=255)
    Sexo = models.TextField(max_length=255)
    documento = models.FileField(upload_to='documentos/')

    def __str__(self):
        return self.nome

    
    

class Curso(models.Model):
    pass


class SorteioCandidato(models.Model):
    pass

class MatriculaAluno(models.Model):
    pass