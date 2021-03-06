 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_paintings, name='paintings'),
    path('<int:painting_id>', views.product_detail, name='product_detail'),
     path('create/', views.add_painting, name='add_painting'),
      path('edit/<int:painting_id>/', views.edit_painting, name='edit_painting'),
      path('delete/<int:painting_id>/', views.delete_painting, name='delete_painting'),
    
    
]