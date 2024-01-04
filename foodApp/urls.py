from django.contrib import admin
from django.urls import path
import foodApp.views

urlpatterns = [
    path('', foodApp.views.index, name="foodApp"),
    path('kyosuke/', foodApp.views.kyosuke, name='kyosuke'),
    path('hayashida/', foodApp.views.hayashida, name='hayashida'),
    path('kyosuke_Photo/', foodApp.views.kyosuke_Photo, name='kyosuke_Photo'),
    path('kyosuke_Comment/', foodApp.views.kyosuke_Comment, name='kyosuke_Comment'),
    path("helspo/", foodApp.views.helspo, name="helspo"),
    path("helspo_comment/", foodApp.views.helspo_comment, name="helspo_comment"),
    path("helspo_photo/", foodApp.views.helspo_photo, name="helspo_photo"),
    path("template/", foodApp.views.template, name="template"),
    path("wellb/", foodApp.views.wellb, name="wellb"),
    path("wellb_comment/", foodApp.views.wellb_comment, name="wellb_comment"),
    path("wellb_photo/", foodApp.views.wellb_photo, name="wellb_photo"),
    path("tonnya/", foodApp.views.tonnya, name="tonnya"),
    path("manngetu/", foodApp.views.manngetu, name="manngetu"),
    path("danbo/", foodApp.views.danbo, name="danbo"),
    path("iki/", foodApp.views.iki, name="iki"),
    path("ginpu/", foodApp.views.ginpu, name="ginpu"),
    path("himuro/", foodApp.views.himuro, name="himuro"),
    path("matuya/", foodApp.views.matuya, name="matuya"),
]
