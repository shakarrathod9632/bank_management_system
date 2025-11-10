from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('deposit/<int:account_id>/', views.deposit, name='deposit'),
    path('withdraw/<int:account_id>/', views.withdraw, name='withdraw'),
]