from django.shortcuts import render

def index_projet(request):
    return render(request, "base.html")