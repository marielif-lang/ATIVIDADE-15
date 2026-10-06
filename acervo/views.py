from django.shortcuts import render, get_object_or_404
from .models import Livro, Autor

# --- VIEWS DE LIVROS ---
def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'acervo/lista_livros.html', {'livros': livros})

def detalhe_livro(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'acervo/detalhe_livro.html', {'livro': livro})

# --- VIEWS DE AUTORES ---
def lista_autores(request):
    autores = Autor.objects.all()
    return render(request, 'acervo/lista_autores.html', {'autores': autores})

def detalhe_autor(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    return render(request, 'acervo/detalhe_autor.html', {'autor': autor})