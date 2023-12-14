from django.contrib import admin
from django.urls import path
import foodApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', foodApp.views.index, name="foodApp"),
    path('kyosuke/', foodApp.views.kyosuke, name='kyosuke')
]
