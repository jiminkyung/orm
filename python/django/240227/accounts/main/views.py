from django.http import HttpResponse


def index(request):
    return HttpResponse("Index 페이지입니다!")