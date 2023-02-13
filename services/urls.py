from django.urls import path
from services import views

# Url links to services pages
urlpatterns = [
    path('', views.services, name='services'),
]