from django.urls import path
from . import views

urlpatterns = [
    path('product/<int:id>/', views.productPage, name='productPage'),
    path('product/rate_product/<int:id>/', views.rate_product, name='rate_product'),
    path('product/<int:product_id>/add_comment/', views.add_comment, name='add_comment'),
    path('product/comment/<int:comment_id>/admin_reply/', views.admin_reply_comment, name='admin_reply_comment'),
]
