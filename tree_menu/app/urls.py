from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts_view, name='contacts'),
    path('about/', views.about_view, name='about'),
    path('home/', views.home_view, name='home'),
]
