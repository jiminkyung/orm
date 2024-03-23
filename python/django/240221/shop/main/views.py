from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    items = f"<li>베스트 상품</li>" * 10
    return HttpResponse(f"""
<h1>index 페이지 입니다.</h1>
<ol>{items}</ol>
""")

def about(request):
    return HttpResponse("<h1>오름컴퍼니 입니다.</h1>")

def contact(request):
    return HttpResponse("<h1>걸어오시면 됩니다.</h1>")