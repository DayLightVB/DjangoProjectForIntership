from django.urls import path

from . import views

urlpatterns = [
    path('micky/', views.hellomicky, name='hellomicky'),
    path('polls/', views.index, name='index'),
    path('fine/', views.fine, name='fine'),
]