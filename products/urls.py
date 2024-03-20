from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<product_id>', views.product_detail, name='product_detail'),
    path('delete_comment/<int:comment_id>/<int:product_id>/', views.delete_comment,name='delete_comment'),
    path('edit_comment/<int:comment_id>/<int:product_id>/', views.edit_comment,name='edit_comment'),
]