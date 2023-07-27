from django.urls import path
from task_manager.labels.views import LabelsList, \
    CreateLabel, DeleteLabel, UpdateLabel


urlpatterns = [
    path('', LabelsList.as_view(), name='labels'),
    path('create/', CreateLabel.as_view(), name='create_lbl'),
    path('<int:pk>/delete/', DeleteLabel.as_view(), name='delete_lbl'),
    path('<int:pk>/update/', UpdateLabel.as_view(), name='update_lbl'),
]
