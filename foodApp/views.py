from django.shortcuts import render

def index(request):
    return render(request,'foodApp/index.html')

def kyosuke(request):
    return render(request,'foodApp/kyosuke.html')