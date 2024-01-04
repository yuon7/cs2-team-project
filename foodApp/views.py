from django.shortcuts import render, redirect
from django.db.models import Avg
from .forms import ReviewForm
from .models import Restaurant, Review


def get_stars(rating):
    # 星のリストを生成する関数
    stars = '★' * rating + '☆' * (5 - rating)
    return stars


def index(request):
    return render(request, 'foodApp/index.html')


def danbo(request):
    return render(request, 'foodApp/danbo.html')


def hayashida(request):
    restaurant = Restaurant.objects.get(name="はやし田")
    reviews = Review.objects.filter(restaurant=restaurant)
    average_rating = reviews.aggregate(
        Avg('rating'))['rating__avg']  # 評価の平均を計算

    if average_rating is not None:
        average_rating = round(average_rating, 1)  # 平均評価を1桁に丸める
        average_stars = get_stars(round(average_rating))  # 平均評価に対する星を生成
    else:
        average_rating = 'No reviews yet'

    for review in reviews:
        review.stars = get_stars(review.rating)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.save()
            return redirect('hayashida')
    else:
        form = ReviewForm()

    return render(request, 'foodApp/hayashida.html', {
        'restaurant': restaurant,
        'reviews': reviews,
        'average_rating': average_rating,
        'average_stars': average_stars if average_rating != 'No reviews yet' else 'まだレビューがありません',
        'form': form
    })


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


def tonnya(request):
    return render(request, 'foodApp/tonnya.html')


def manngetu(request):
    return render(request, 'foodApp/manngetu.html')


def iki(request):
    return render(request, 'foodApp/iki.html')


def ginpu(request):
    return render(request, "foodApp/ginpu.html")


def himuro(request):
    return render(request, "foodApp/himuro.html")


def matuya(request):
    return render(request, "foodApp/matuya.html")


def natsumi(request):
    return render(request, "foodApp/natsumi.html")
