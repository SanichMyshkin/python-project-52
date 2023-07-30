from django.urls import reverse_lazy
from django.views.generic import CreateView, \
    DeleteView, UpdateView, DetailView
from django_filters.views import FilterView
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin, \
    UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from .filter import TaskFilter
from task_manager.translations.trans import TransMessagesUsers, \
    TransMessagesTemplates, TransMessagesTask


class TasksList(LoginRequiredMixin, FilterView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks/index.html'
    filterset_class = TaskFilter
    login_url = 'user_login'

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)


class ShowTask(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/show_task.html'
    context_object_name = 'task'
    login_url = 'user_login'

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = 'users/create.html'
    success_url = reverse_lazy('tasks_list')
    extra_context = {'header': TransMessagesTask.create_task,
                     'button': TransMessagesTemplates.create_button}
    login_url = 'user_login'

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        messages.success(self.request, TransMessagesTask.success_create)
        return super(CreateTask, self).form_valid(form)


class UpdateTask(LoginRequiredMixin, SuccessMessageMixin,
                 UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = 'users/create.html'
    success_url = reverse_lazy('tasks_list')
    success_message = TransMessagesTask.success_update
    extra_context = {'header': TransMessagesTask.update_task,
                     'button': TransMessagesTemplates.update_button}
    login_url = 'user_login'

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)


class DeleteTask(LoginRequiredMixin, SuccessMessageMixin,
                 UserPassesTestMixin, DeleteView):
    model = Task
    login_url = 'user_login'
    success_url = reverse_lazy('tasks_list')
    template_name = 'users/delete.html'
    success_message = TransMessagesTask.success_delete
    extra_context = {'header': TransMessagesTask.to_del_task,
                     'button': TransMessagesTemplates.confirm_delete}

    def test_func(self):
        task = self.get_object()
        return self.request.user.id == task.author.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            message = TransMessagesTask.no_delete_task
            url = reverse_lazy('tasks_list')
        else:
            message = TransMessagesUsers.no_login
            url = self.login_url
        messages.warning(self.request, message)
        return redirect(url)
