from django.shortcuts import render
from  django.http import  HttpResponse

# Create your views here.


def contactus(request):
    return HttpResponse("---- welcome to contactus page ")