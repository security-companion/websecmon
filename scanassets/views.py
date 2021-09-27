from django.shortcuts import render
from django.http import HttpResponse

scanassetsList =[
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'desc1'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'desc2'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'desc3'
    },
]


def scanassets(request):
    msg = 'scanassets'
    number = 10
    context = {'message': msg, 'number': number, 'scanassets': scanassetsList }
    return render(request, 'scanassets/scanassets.html', context)

def scanasset(request, pk):
    scanassetObj = None
    for i in scanassetsList:
        if i['id'] == pk:
            scanassetObj = i
    return render(request, 'scanassets/single-scanasset.html', {'scanasset': scanassetObj})