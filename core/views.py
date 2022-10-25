from django.shortcuts import render, HttpResponse


#Criação de função e visualizações dos client
def index(request):
    return HttpResponse('Hello World!!')
def soma(request, x, y):
    return HttpResponse('Soma: {} '.format(x+y))

def subtracao(request, x, y):
    return HttpResponse('Subtração: {} '.format(x-y))

def multiplicacao(request, x, y):
    return HttpResponse('Multiplicacao: {} '.format(x*y))

def divisao(request, x, y):
    return HttpResponse('Divisão: {} '.format(x/y))




