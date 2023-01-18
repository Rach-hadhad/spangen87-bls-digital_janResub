from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('add/', views.add_product, name='add_product'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path(
        'delete/<int:product_id>/',
        views.delete_product,
        name='delete_product'),
    path('stock/', views.stock_levels, name='stock_levels'),
    path(
        'stock/update/<int:product_id>/',
        views.update_stock,
        name='update_stock'),
    path('review/<int:product_id>/', views.give_review, name='give_review'),
]
