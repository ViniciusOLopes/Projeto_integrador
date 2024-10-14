from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import UsuariosForm
from .models import Usuarios

def coleta_dados_usuario(request):
    if request.method == "POST":
        form = UsuariosForm(request.POST, request.FILES)  # Inclui arquivos
        if form.is_valid():
            form.save()  # Salva os dados no banco
            return redirect('sucesso')  # Redireciona para uma página de sucesso
    else:
        form = UsuariosForm()
    return render(request, 'cadastro.html', {'form': form})

def criacao_cursos(request):
    return render(request, 'curso.html')

def inscricao (request):
    return render(request, 'inscricao.html') 

def sorteio_aluno(request):
    alunos = Usuarios.object.all()

    if alunos.exists():
        aluno_sorteio = random.choice(alunos)
    else:
        aluno_sorteio = None
    return render(request,'sorteio.html', {'aluno_sorteado':aluno_sorteio})

