from django.contrib import admin
from django.urls import path,include
import foodApp.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("foodApp.urls"))
]
