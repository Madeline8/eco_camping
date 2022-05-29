from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('newsletter_subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
]
