from django.http import HttpResponse
from django.shortcuts import render

def home(request):
   # return HttpResponse("Hello,World! You are at chai aur Django home page.")
   return render(request, 'index.html')

def about(request):
    return HttpResponse("Hello,World! You are at chai aur Django about Page.")

def contact(request):
    return HttpResponse("Hello,World! You are at chai aur Django contact page.")


