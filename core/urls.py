from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('coc/', views.coc, name='coc'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.events, name='events'),
    path('join/', views.join, name='join'),
    path('partners/', views.partners, name='partners'),
    path('resources/', views.resources, name='resources'),
    path('values/', views.values, name='values'),
]
