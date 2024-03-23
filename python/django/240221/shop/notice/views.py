from django.shortcuts import render
from django.http import HttpResponse

def notice(request):
    return HttpResponse("<h1><a href='free/'>자유게시판</a> / <a href='onenone/'>일대일상담</a></h1>")

def free(request):
    return HttpResponse("<h2>자유게시판</h2>")

def free_details(request, pk):
    return HttpResponse(f"<h3>{pk}번째 자유게시판 글입니다.")

def onenone(request):
    return HttpResponse("<h2>일대일상담</h2>")

def onenone_details(request, pk):
    return HttpResponse(f"<h3>{pk}번째 일대일상담 글입니다.")