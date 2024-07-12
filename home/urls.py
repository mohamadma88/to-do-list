from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.addtask, name='task'),
    path('delete/<int:pk>', views.deleteTask, name='delete')
]
