from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Producto
from .forms import ProductForm
from django.http import HttpResponseRedirect

def hello_world(reqest):
    producto = Producto.objects.order_by('id')
    templates = loader.get_template('index.html')
    context = {
        'producto' : producto
    }
    return  HttpResponse(templates.render(context, reqest))


def agregar_producto(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            producto = form.save()  
            producto.save()  
            return HttpResponseRedirect('/')
    else:
        form = ProductForm()
    template = loader.get_template('agregar.html')
    context = {
        'form' : form
    }
    return HttpResponse(template.render(context,request))
