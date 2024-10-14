from django.shortcuts import render, redirect
from django.shortcuts import render
from .forms import UsuariosForm

def coleta_dados_usuario(request):
    if request.method == "POST":
        form = UsuariosForm(request.POST, request.FILES)  # Inclui arquivos
        if form.is_valid():
            form.save()  # Salva os dados no banco
            return redirect('sucesso')  # Redireciona para uma página de sucesso
    else:
        form = UsuariosForm()
    return render(request, 'cadastro.html', {'form': form})



def Inscricao (request, id_curso):
    return render(request, 'cadastro.html')  # Certifique-se de que index.html existe na pasta de templates
