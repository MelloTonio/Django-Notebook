from django.shortcuts import render
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.contrib import messages



# Create your views here.
def index(request):

    contatos = Contato.objects.order_by('-id')
    paginator = Paginator(contatos,5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request,'contatos/index.html',{
        'contatos': contatos
    })

def ver_contato(request,contato_id):
    try:
        contato = Contato.objects.get(id=contato_id)
        if not contato.mostrar:
            raise Http404()
        return render(request,'contatos/ver_contato.html',{
            'contato':contato
        })
    except Contato.DoesNotExist as e:
        raise Http404()

def ver_categoria(request,contato_string):
    contato = Contato.objects.get(id=contato_string)

    return render(request,'contatos/contato_categoria.html',{
        'contato': contato
    })

def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(request,messages.ERROR,'Campo não pode ser vazio!')
    contatos = Contato.objects.order_by('-id').filter(nome__icontains=termo)
    paginator = Paginator(contatos,5)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request,'contatos/busca.html',{
        'contatos': contatos
    })

def ver_sobre(request):

    return render(request,'contatos/sobre.html')