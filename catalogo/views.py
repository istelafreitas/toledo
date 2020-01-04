from django.shortcuts import render
from .models import Produto


def catalogo(request):

    produto = Produto.objects.all()
    print(produto.query)
    return render(request, 'list.html', {'produto':produto})
