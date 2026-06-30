from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(requests):
    return HttpResponse('<h1>welcome to catalyst\'s home page</h1>')

def about(requests):
    return HttpResponse('<h1>here\'s a little information about us</h1>')

def contact(requests):
    return HttpResponse('<h1>get in touch with us</h1>')

