from django.shortcuts import render
from django.http import HttpResponse

def product(request):
    return HttpResponse("<h1>상품게시판</h2>")

def product_details(request, pk):
    return HttpResponse(f"{pk}번째 상품")