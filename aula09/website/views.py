from django.shortcuts import render

# Create your views here.

def home (request):
    nome = 'Paulo'
    idade = 22
    lista_roupas = [
        'Bone da lacoste'
        'calça'
        'cueca'
        'tenis'
    ]

    argumentos = {
        'roupas' : lista_roupas,
        'nomes' : nome,
        'idade': idade
    }
    return render(request,'home.html',argumentos)