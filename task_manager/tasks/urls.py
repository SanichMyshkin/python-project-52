from django.urls import path
from task_manager.tasks.views import TasksList, \
    CreateTask, DeleteTask, UpdateTask, ShowTask


urlpatterns = [
    path('', TasksList.as_view(), name='tasks_list'),
    path('create/', CreateTask.as_view(), name='create_tsk'),
    path('<int:pk>/delete/', DeleteTask.as_view(), name='delete_tsk'),
    path('<int:pk>/update/', UpdateTask.as_view(), name='update_tsk'),
    path('<int:pk>/', ShowTask.as_view(), name='show_task'),
]
