from django.urls import path
from . import views

app_name = 'buy'
urlpatterns = [
    path('create/', views.order_create, name='order_create'),
]
