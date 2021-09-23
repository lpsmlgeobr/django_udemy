from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
dic = {"january":"vem que vem", "february": "Teve bom", "march":"nois"}


def index(request):
    list_items = ""
    for key in dic.keys():
        capitalized_month = key.capitalize()
        month_path = reverse("month-challenge", args=[key])
        list_items += f"<li><a href = \"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_number(request,month):
    
    
    months = list(dic.keys())
    if month >len(months):
        return HttpResponseNotFound("Invalid month")
    fw_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[fw_month]) #/challenge/january
    return HttpResponseRedirect(redirect_path)

def months(request, month):
    try:
        challenge_text = dic[month]
        response_data = f"<h2>{challenge_text}<h2>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>Tem esse mês não!<h1>")

