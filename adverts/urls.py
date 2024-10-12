from django.urls import path
from . import views

urlpatterns = [
    path('adverts/', views.advert_list, name='advert_list'),
    path('', views.home, name= 'home'),
    path('create/', views.create_advert, name='create_advert'),
]
