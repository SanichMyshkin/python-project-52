from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, \
    DeleteView, UpdateView
from .models import Label
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from task_manager.translations.trans import TransMessagesLabels, \
    TransMessagesUsers, TransMessagesTemplates


class LabelsList(LoginRequiredMixin, ListView):
    model = Label
    context_object_name = 'labels'
    template_name = 'labels/index.html'
    login_url = 'user_login'

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)


class CreateLabel(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = 'users/create.html'
    success_url = reverse_lazy('labels')
    login_url = 'user_login'
    success_message = TransMessagesLabels.success_create
    extra_context = {'header': TransMessagesLabels.create_label,
                     'button': TransMessagesTemplates.create_button}

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesLabels.success_create)
        return redirect(self.login_url)


class UpdateLabel(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    fields = ['name']
    login_url = 'user_login'
    template_name = 'users/create.html'
    success_url = reverse_lazy('labels')
    success_message = TransMessagesLabels.success_update
    extra_context = {'header': TransMessagesLabels.update_label,
                     'button': TransMessagesTemplates.update_button}

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)


class DeleteLabel(LoginRequiredMixin, DeleteView):
    model = Label
    login_url = 'user_login'
    success_url = reverse_lazy('labels')
    template_name = 'users/delete.html'
    extra_context = {"header": TransMessagesLabels.to_del_label,
                     'button': TransMessagesTemplates.delete_button}

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, TransMessagesLabels.success_delete)
        except ProtectedError:
            messages.warning(self.request, TransMessagesLabels.no_delete_label)
        finally:
            return redirect(success_url)
