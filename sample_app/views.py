from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Go to http://127.0.0.1:8000/admin/sample_app/page/add/ with credentials admin/admin")
