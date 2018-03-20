from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Producto

def hello_world(reqest):
    producto = Producto.objects.order_by('id')
    templates = loader.get_template('index.html')
    context = {
        'producto' : producto
    }
    return  HttpResponse(templates.render(context, reqest))
