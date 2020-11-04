from django.urls import path

from . import views

urlpatterns = [
    path('klo/', views.klo, name='klo'),
    path('offers/', views.offers, name='offers'),
    path('about/', views.about, name='about'),
    path('signup/', views.signup, name='signup'),
]