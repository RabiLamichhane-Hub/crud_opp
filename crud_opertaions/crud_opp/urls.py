from django.urls import path
from . import views

urlpatterns = [
    path('', views.read, name='read'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('crud_opp/<int:pk>/description_view/', views.description_view, name='description_view'),
]