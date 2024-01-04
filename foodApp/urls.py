from django.contrib import admin
from django.urls import path
import foodApp.views

urlpatterns = [
    path('', foodApp.views.index, name="foodApp"),
    path('kyosuke/', foodApp.views.kyosuke, name='kyosuke'),
    path('hayashida/', foodApp.views.hayashida, name='hayashida'),
    path("helspo/", foodApp.views.helspo, name="helspo"),
    path("template/", foodApp.views.template, name="template"),
    path("wellb/", foodApp.views.wellb, name="wellb"),
    path("tonnya/", foodApp.views.tonnya, name="tonnya"),
    path("manngetu/", foodApp.views.manngetu, name="manngetu"),
    path("danbo/", foodApp.views.danbo, name="danbo"),
    path("iki/", foodApp.views.iki, name="iki"),
    path("ginpu/", foodApp.views.ginpu, name="ginpu"),
    path("himuro/", foodApp.views.himuro, name="himuro"),
    path("matuya/", foodApp.views.matuya, name="matuya"),
    path("natsumi/", foodApp.views.natsumi, name="natsumi"),
]
