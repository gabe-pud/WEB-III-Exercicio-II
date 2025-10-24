from django.shortcuts import render, redirect
from app.models import Desenvolvedor, Contato
from app.forms import FormDesenvolvedor, FormContato



# Create your views here.

def index(request):
    return render(request, 'index.html')
    
def sobre(request):
    return render(request, 'sobre.html')

def dev(request):
    devs = Desenvolvedor.objects.all().values()
    return render(request, 'desenvolvedores.html',{'desenvolvedores':devs})

def excluirDev(request, id_dev):
    dev = Desenvolvedor.objects.get(id=id_dev)
    dev.delete()
    return redirect('dev')

def salvarDev(request):
   formulario = FormDesenvolvedor(request.POST or None)
   if request.POST:
       if formulario.is_valid():
           formulario.save()
           return redirect('dev')
   return render(request, 'salvardev.html', {"form":formulario})

def editarDev(request, id_dev):
    dev = Desenvolvedor.objects.get(id=id_dev)
    formulario = FormDesenvolvedor(request.POST or None, instance=dev)
    if request.POST:
       if formulario.is_valid():
           formulario.save()
           return redirect('dev')
    return render(request, 'editardev.html', {"form":formulario})

# contatos
def contato(request):
    contato = Contato.objects.all().values()
    return render(request, 'contato.html',{'contatos':contato})

def salvarContato(request):
   formulario = FormContato(request.POST or None)
   if request.POST:
       if formulario.is_valid():
           formulario.save()
           return redirect('contato')
   return render(request, 'salvarContato.html', {"form":formulario})

def excluirContato(request, id_contato):
    contato = Contato.objects.get(id=id_contato)
    contato.delete()
    return redirect('contato')