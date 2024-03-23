from django.shortcuts import render
from products import products


def product_list(request):
    context = { "product_list": products }
    return render(request, "product/product_list.html", context)


def product_details(request, pk):
    context = { "product": products[pk-1] }
    return render(request, "product/product_details.html", context)
