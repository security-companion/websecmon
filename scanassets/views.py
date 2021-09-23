from django.shortcuts import render
from django.http import HttpResponse

def scanassets(request):
    return HttpResponse('Here are our scanassets')

def scanasset(request, pk):
    return HttpResponse('Single asset' + pk)