from django.shortcuts import render
# Create your views here.

def plantilla (request):
    return render(request,'contacto.html')


def planilla (request):
    return render(request,'turismo.html')