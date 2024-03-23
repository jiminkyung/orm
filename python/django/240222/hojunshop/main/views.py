from django.shortcuts import render
from products import products

def index(request):
    topsix = sorted(products, key=lambda x: x["sold"], reverse=True)[:6]
    context = { "topsix": topsix }
    return render(request, "main/index.html", context)

def about(request):
    return render(request, "main/about.html")