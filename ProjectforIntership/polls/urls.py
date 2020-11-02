from django.urls import path

from . import views

urlpatterns = [
    path('klo/', views.main_home, name='klo'),
    path('offers/', views.offers, name='offers'),
    path('about/', views.about, name='about'),
]