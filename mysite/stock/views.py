from django.shortcuts import render
from django.http import HttpResponse
import tushare as ts
# Create your views here.

def home(request):
	return HttpResponse("Hello World")

