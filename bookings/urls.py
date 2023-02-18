from django.urls import path
from bookings import views

# Url links to bookings pages
urlpatterns = [
    path('', views.bookings, name='bookings'),
    path('add/', views.add_bookings, name='add_bookings'),
]
