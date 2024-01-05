from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('<str:pk>/', views.detail, name='detail'),
    path('<str:pk>/delete/', views.delete, name='delete'),
    path('<str:pk>/edit/', views.edit, name='edit')
]
