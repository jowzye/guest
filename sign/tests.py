from django.shortcuts import render
from django.test import TestCase
from sign import views
# Create your tests here.
def index(request):
    return render(request,"index.html")