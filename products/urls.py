from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('catalog/', views.product_list, name='product_list'),
    path('catalog/category/<int:category_id>/', views.product_list, name='product_list_by_category'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
]