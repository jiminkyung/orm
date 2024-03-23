from django.shortcuts import render
from django.http import HttpResponse

def qna(request):
    return HttpResponse("<h1>Q&A</h1>")

def qna_details(request, pk):
    return HttpResponse(f"{pk}번째 Q&A글입니다.")