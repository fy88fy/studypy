from django.shortcuts import render,HttpResponse,redirect

# Create your views here.


def list(request):
    return HttpResponse('<h1>list</h1>')

def add(request):
    return HttpResponse('<h1>add</h1>')

def update(request,num):
    print ('delete----',num)
    return HttpResponse('<h1>update</h1>')

def delete(request):
    return HttpResponse('<h1>delete</h1>')