from django.contrib import admin
from django.urls import path, include

from task_manager import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),

    path('users/', include('task_manager.users.urls')),
    path('statuses/', include('task_manager.statuses.urls')),

    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.UserLogoutView.as_view(), name='user_logout'),
    path('admin/', admin.site.urls),
]
