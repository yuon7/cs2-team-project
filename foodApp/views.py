from django.shortcuts import render, redirect
from django.db.models import Avg
from .forms import ReviewForm
from .models import Restaurant, Review


def get_star_rating(rating):
    if rating:
        return int(rating) * "★" + (5 - int(rating)) * "☆"
    else:
        return "レビューなし"


def index(request):
    restaurants = Restaurant.objects.filter(
        name__in=["はやし田", "暖母", "赤羽京介", "Helspo食堂"])
    ratings = {
        restaurant.slug: get_star_rating(Review.objects.filter(
            restaurant=restaurant).aggregate(Avg('rating'))['rating__avg'])
        for restaurant in restaurants
    }
    return render(request, 'foodApp/index.html', ratings)


def danbo(request):
    danbo = Restaurant.objects.get(name="暖母")
    reviews = Review.objects.filter(restaurant=danbo)
    average_rating = reviews.aggregate(
        Avg('rating'))['rating__avg']  # 評価の平均を計算

    if average_rating is not None:
        average_rating = round(average_rating, 1)
        average_stars = get_star_rating(round(average_rating))
    else:
        average_rating = 'No reviews yet'

    for review in reviews:
        review.stars = get_star_rating(review.rating)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = danbo
            review.save()
            return redirect('danbo')
    else:
        form = ReviewForm()

    return render(request, 'foodApp/danbo.html', {
        'restaurant': danbo,
        'reviews': reviews,
        'average_rating': average_rating,
        'average_stars': average_stars if average_rating != 'No reviews yet' else 'まだレビューがありません',
        'form': form
    })


def hayashida(request):
    hayashida = Restaurant.objects.get(name="はやし田")
    reviews = Review.objects.filter(restaurant=hayashida)
    average_rating = reviews.aggregate(
        Avg('rating'))['rating__avg']  # 評価の平均を計算

    if average_rating is not None:
        average_rating = round(average_rating, 1)
        average_stars = get_star_rating(round(average_rating))
    else:
        average_rating = 'No reviews yet'

    for review in reviews:
        review.stars = get_star_rating(review.rating)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = hayashida
            review.save()
            return redirect('hayashida')
    else:
        form = ReviewForm()

    return render(request, 'foodApp/hayashida.html', {
        'restaurant': hayashida,
        'reviews': reviews,
        'average_rating': average_rating,
        'average_stars': average_stars if average_rating != 'No reviews yet' else 'まだレビューがありません',
        'form': form
    })


def kyosuke(request):
    return render(request, 'foodApp/kyosuke.html')


def helspo(request):
    return render(request, 'foodApp/helspo.html')


def template(request):
    return render(request, 'foodApp/template.html')


def wellb(request):
    return render(request, 'foodApp/wellb.html')


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
