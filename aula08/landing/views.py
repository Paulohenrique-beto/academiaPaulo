from django.shortcuts import render

# Create your views here.
def mostra_index(request):
    return render(request, 'index.html')

def mostra_sobre(request):
    return render(request, 'sobre.html')