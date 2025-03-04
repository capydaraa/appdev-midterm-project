from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task_update/<int:pk>/', views.task_update, name='task_update'),
    path('task_delete/<int:pk>/', views.task_delete, name='task_delete'),
    path('task/toggle_status/<int:pk>/', views.toggle_status, name='toggle_status'),
]
