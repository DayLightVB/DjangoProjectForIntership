from django.urls import path
from . import views

urlpatterns = [
    path('', views.klo, name='klo'),
    path('offers/', views.offers, name='offers'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('<int:pk>', views.AdDetailView.as_view(), name='ad-detail'),
    path('<int:pk>/update', views.AdUpdateView.as_view(), name='ad-update'),
    path('<int:pk>/delete', views.AdDeleteView.as_view(), name='ad-delete')
]