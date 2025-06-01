from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('envoyer/', views.envoyer_messages, name='envoyer'),
]
