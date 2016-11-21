from django.shortcuts import render, render_to_response
from django.http import HttpResponse


def index(request):
    return render_to_response("index.html")
def faq(request):
    return render_to_response("faq.html")
def services(request):
	return render_to_response("services.html")
def login(request):
	return render_to_response("login.html")



# Create your views here.
