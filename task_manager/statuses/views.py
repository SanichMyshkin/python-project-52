from django.shortcuts import redirect
from task_manager.statuses.models import Status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, \
    DeleteView, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect
from task_manager.translations.trans import TransMessagesTemplates, \
    TransMessagesUsers, TransMessagesStatus


# Create your views here.

class StatusView(LoginRequiredMixin, ListView):
    model = Status
    context_object_name = 'statuses'
    template_name = 'statuses/index.html'
    login_url = 'user_login'
    extra_context = {
        'header': TransMessagesTemplates.status,
        'button': TransMessagesTemplates.create_status
    }

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    login_url = 'user_login'
    fields = ['name']
    template_name = 'users/create.html'
    success_url = reverse_lazy('statuses')
    success_message = TransMessagesStatus.create_success

    extra_context = {'header': TransMessagesTemplates.create_status,
                     'button': TransMessagesTemplates.create_button
                     }

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)


class StatusDestroyView(LoginRequiredMixin, DeleteView):
    model = Status
    login_url = 'user_login'
    success_url = reverse_lazy('statuses')
    template_name = 'users/delete.html'
    extra_context = {'header': TransMessagesTemplates.delete_status,
                     'button': TransMessagesTemplates.delete_button
                     }

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.success(self.request, TransMessagesStatus.delete_success)
        except ProtectedError:
            messages.warning(self.request, TransMessagesStatus.no_rule_delete)
        finally:
            return HttpResponseRedirect(success_url)


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    login_url = 'user_login'
    fields = ['name']
    template_name = 'users/create.html'
    success_url = reverse_lazy('statuses')
    success_message = TransMessagesStatus.update_success

    extra_context = {'header': TransMessagesTemplates.update_status,
                     'button': TransMessagesTemplates.update_button
                     }

    def handle_no_permission(self):
        messages.warning(self.request, TransMessagesUsers.no_login)
        return redirect(self.login_url)
