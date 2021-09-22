from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def months(request, month):
    dic = {"january":"vem que vem", "february": "Teve bom", "march":"nois"}
    if month in dic.keys():
        return HttpResponse(dic[month])
    else:
        return HttpResponseNotFound("Tem esse mês não!")

