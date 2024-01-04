from django.shortcuts import render


def index(request):
    return render(request, 'foodApp/index.html')


def hayashida(request):
    return render(request, 'foodApp/hayashida.html')


def kyosuke(request):
    return render(request, 'foodApp/kyosuke.html')


def kyosuke_Photo(request):
    return render(request, 'foodApp/kyosuke_Photo.html')


def kyosuke_Comment(request):
    return render(request, 'foodApp/kyosuke_Comment.html')


def helspo(request):
    return render(request, 'foodApp/helspo.html')


def helspo_comment(request):
    return render(request, "foodApp/helspo_comment.html")


def helspo_photo(request):
    return render(request, "foodApp/helspo_photo.html")


def template(request):
    return render(request, 'foodApp/template.html')


def wellb(request):
    return render(request, 'foodApp/wellb.html')


def wellb_comment(request):
    return render(request, "foodApp/wellb_comment.html")


def wellb_photo(request):
    return render(request, "foodApp/wellb_photo.html")
