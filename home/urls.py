from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('price_list', views.price_list, name="price_list"),
    # path('gallery', views.gallery, name="gallery"),
]
