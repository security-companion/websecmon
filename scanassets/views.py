from django.shortcuts import render
from django.http import HttpResponse

def scanassets(request):
    return render(request, 'scanassets.html')

def scanasset(request, pk):
    return render(request, 'single-scanasset.html')