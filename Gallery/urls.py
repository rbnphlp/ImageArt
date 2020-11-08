 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_paintings, name='paintings'),
    path('<painting_id>', views.product_detail, name='product_detail'),
]