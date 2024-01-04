from django.contrib import admin
from django.urls import path
import foodApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', foodApp.views.index, name="foodApp"),
    path('kyosuke/', foodApp.views.kyosuke, name='kyosuke'),
    path('kyosuke_Photo/', foodApp.views.kyosuke_Photo, name='kyosuke_Photo'),
    path('kyosuke_Comment/', foodApp.views.kyosuke_Comment, name='kyosuke_Comment'),
    path("helspo/",foodApp.views.helspo,name="helspo"),
    path("template/", foodApp.views.template, name="template"),
    path("wellb/",foodApp.views.wellb,name="wellb"),
    path("tonnya/",foodApp.views.tonnya,name="tonnya"),
    path("manngetu/",foodApp.views.manngetu,name="manngetu"),
    path('<int:article_id>/', foodApp.views.detail, name='detail'),
]