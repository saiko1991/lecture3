from django.urls import path
from . import views

app_name = "tasks"

urlpatterns = [
    path('', views.index, name='tasks_index'),
    path('add',views.add,name='add_task'),
]