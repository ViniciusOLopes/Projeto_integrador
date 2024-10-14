from django.db import models
from django.contrib.auth.models import  User
from django.core.exceptions import ValidationError
import dns.resolver
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


#Classe que verifica se o dominio e valido
class CheckDns(email):
    dominio = email.split('@')[1]
    try: 
        dns.resolver.resolve(dominio, 'MX')
    except dns.resolver.NXDOMAIN:
        raise ValidationError(f'O domínio {dominio} não possui registros MX válidos.')
    except dns.resolver.LifetimeTimeout:
        raise ValidationError("Não foi possível contactar ao DNS")
    except Exception as e:  # Captura qualquer outra exceção
        raise ValidationError(f"Ocorreu um erro ao validar o domínio {dominio}")


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    CPF = models.TextField(max_length=255)
    RG = models.TextField(max_length=255)
    Orgao = models.TextField(max_length=255)
    Emissao = models.DateField()  # Corrigido
    email = models.EmailField(validators=[CheckDns])#O email ira chamar a classe que ira verificar seu dominio
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

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    nome = models.TextField(max_length= 255)
    carga_horaria = models.TextField(max_length=255)
    descricao= models.TextField(max_length=255)
    id_curso = models.TextField(primary_key= True)
    criado_por = models.ForeignKey(Usuarios, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Matricula_Aluno(models.Model):
    aluno = models.ForeignKey(Usuarios, on_delete= models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete= models.CASCADE)
    data_matricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.aluno.nome} esta matriculada(o) no curso {self.curso.nome}"
    

    