from django.shortcuts import render

def index(request):
    return render(request,'foodApp/index.html')

def kyosuke(request):
    return render(request,'foodApp/kyosuke.html')


def kyosuke_Photo(request):
    return render(request, 'foodApp/kyosuke_Photo.html')

def kyosuke_Comment(request):
    return render(request, 'foodApp/kyosuke_Comment.html')

def helspo(request):
    return render(request,'foodApp/helspo.html')