from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    temp = "temporário"
    context = {"temp": temp}
    return render(request, "finapp/index.html", context)