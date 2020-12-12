from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [
    path('', views.product_list1, name='product_list'),
    path('<slug:category_slug>/', views.product_list_by_category, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    # path('<int:category>', views.category_list)
]
