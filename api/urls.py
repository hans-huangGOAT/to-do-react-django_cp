from django.urls import path
from .views import *

urlpatterns = [
    path('', api_over_view, name='api_over_view'),
    path('task-detail/<str:pk>/', task_detail, name='task_detail'),
    path('task-update/<str:pk>/', task_update, name='task_update'),
    path('task-delete/<str:pk>/', task_delete, name='task_delete'),
    path('task-list/', task_list, name='task_list'),
    path('task-create/', task_create, name='task_create'),
]