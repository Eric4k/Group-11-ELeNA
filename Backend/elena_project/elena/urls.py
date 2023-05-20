from django.urls import path
from . import views

urlpatterns = [
     path('route/get/', views.getRoute),
     path('city/post/', views.changeCity)
]
