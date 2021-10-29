from django.shortcuts import render
from django.http import HttpResponse
def first(req):
    return HttpResponse('hey im working')
