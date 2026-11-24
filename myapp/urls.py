from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('add/', views.add_item, name='add_item'),
    path('register/', views.register, name='register'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]
