
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index), #/challenges/
    path("<int:month>", views.monthly_number),
    path("<str:month>",views.months, name="month-challenge")

]