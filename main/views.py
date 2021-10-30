from django.shortcuts import render
from django.http import HttpResponse
def first(req):
    return render(req,'home.html')
