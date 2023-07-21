from django.urls import path

from task_manager.users.views import UsersView, UsersFormCreateView, \
    UsersDestroyView, UsersUpdateView

urlpatterns = [
    path('', UsersView.as_view(), name='users'),
    path('create/', UsersFormCreateView.as_view(), name='user_create'),
    path('<int:pk>/update/', UsersUpdateView.as_view(), name="user_update"),
    path('<int:pk>/delete/', UsersDestroyView.as_view(), name='user_delete'),
]
