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
    kyosuke = Restaurant.objects.get(name="赤羽京介")
    kyosuke_reviews = Review.objects.filter(restaurant=kyosuke)
    average_rating = kyosuke_reviews.aggregate(
        Avg('rating'))['rating__avg']

    if average_rating is not None:
        average_rating = round(average_rating, 1)
        average_stars = get_star_rating(round(average_rating))
    else:
        average_rating = 'No reviews yet'

    for review in kyosuke_reviews:
        review.stars = get_star_rating(review.rating)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = kyosuke
            review.save()
            return redirect('kyosuke')
    else:
        form = ReviewForm()

    return render(request, 'foodApp/kyosuke.html', {
        'restaurant': kyosuke,
        'reviews': kyosuke_reviews,
        'average_rating': average_rating,
        'average_stars': average_stars if average_rating != 'No reviews yet' else 'まだレビューがありません',
        'form': form
    })


def helspo(request):
    helspo = Restaurant.objects.get(name="Helspo食堂")
    helspo_reviews = Review.objects.filter(restaurant=helspo)
    average_rating = helspo_reviews.aggregate(
        Avg('rating'))['rating__avg']

    if average_rating is not None:
        average_rating = round(average_rating, 1)
        average_stars = get_star_rating(round(average_rating))
    else:
        average_rating = 'No reviews yet'

    for review in helspo_reviews:
        review.stars = get_star_rating(review.rating)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = helspo
            review.save()
            return redirect('helspo')
    else:
        form = ReviewForm()

    return render(request, 'foodApp/helspo.html', {
        'restaurant': helspo,
        'reviews': helspo_reviews,
        'average_rating': average_rating,
        'average_stars': average_stars if average_rating != 'No reviews yet' else 'まだレビューがありません',
        'form': form
    })


def template(request):
    return render(request, 'foodApp/template.html')


def wellb(request):
    wellb = Restaurant.objects.get(name="WellB食堂")
    wellb_reviews = Review.objects.filter(restaurant=wellb)
    average_rating = wellb_reviews.aggregate(
        Avg('rating'))['rating__avg']

    if average_rating is not None:
        average_rating = round(average_rating, 1)
        average_stars = get_star_rating(round(average_rating))
    else:
        average_rating = 'No reviews yet'

    for review in wellb_reviews:
        review.stars = get_star_rating(review.rating)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = wellb
            review.save()
            return redirect('wellb')
    else:
        form = ReviewForm()

    return render(request, 'foodApp/wellb.html', {
        'restaurant': wellb,
        'reviews': wellb_reviews,
        'average_rating': average_rating,
        'average_stars': average_stars if average_rating != 'No reviews yet' else 'まだレビューがありません',
        'form': form
    })


def tonnya(request):
    tonya = Restaurant.objects.get(name="赤羽京介")
    tonya_reviews = Review.objects.filter(restaurant=kyosuke)
    average_rating = tonya_reviews.aggregate(
        Avg('rating'))['rating__avg']

    if average_rating is not None:
        average_rating = round(average_rating, 1)
        average_stars = get_star_rating(round(average_rating))
    else:
        average_rating = 'No reviews yet'

    for review in tonya_reviews:
        review.stars = get_star_rating(review.rating)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = tonya
            review.save()
            return redirect('tonnya')
    else:
        form = ReviewForm()

    return render(request, 'foodApp/kyosuke.html', {
        'restaurant': tonya,
        'reviews': tonya_reviews,
        'average_rating': average_rating,
        'average_stars': average_stars if average_rating != 'No reviews yet' else 'まだレビューがありません',
        'form': form
    })


def manngetu(request):
    tonya = Restaurant.objects.get(name="赤羽京介")
    tonya_reviews = Review.objects.filter(restaurant=kyosuke)
    average_rating = tonya_reviews.aggregate(
        Avg('rating'))['rating__avg']

    if average_rating is not None:
        average_rating = round(average_rating, 1)
        average_stars = get_star_rating(round(average_rating))
    else:
        average_rating = 'No reviews yet'

    for review in tonya_reviews:
        review.stars = get_star_rating(review.rating)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = tonya
            review.save()
            return redirect('tonnya')
    else:
        form = ReviewForm()

    return render(request, 'foodApp/kyosuke.html', {
        'restaurant': tonya,
        'reviews': tonya_reviews,
        'average_rating': average_rating,
        'average_stars': average_stars if average_rating != 'No reviews yet' else 'まだレビューがありません',
        'form': form
    })


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
